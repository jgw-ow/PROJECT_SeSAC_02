import requests
import pandas as pd
import streamlit as st
import altair as alt

# 데이터 가져오기 함수
def fetch_data(api_url):
    """API에서 데이터를 가져와 DataFrame으로 변환"""
    response = requests.get(api_url)
    data = response.json()
    if 'priceInfos' in data:
        price_infos = data['priceInfos']
        dates = [item['localDate'] for item in price_infos]
        prices = [item['closePrice'] for item in price_infos]
        df = pd.DataFrame({'날짜': dates, '종가 (KRW)': prices})
        df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m%d')
        return df.set_index('날짜')
    else:
        return None

# 시각화 함수 (Altair 사용하여 넓이 조정)
def display_combined_chart(api_urls, selected_period):
    """여러 지수를 하나의 차트에 표시 (Altair 사용)"""
    all_data = {}  # KRW 데이터를 담을 딕셔너리

    # 각 지수 데이터를 가져와서 하나의 DataFrame에 통합
    for label, urls in api_urls.items():
        data = fetch_data(urls[selected_period])
        if data is not None:
            all_data[label] = data['종가 (KRW)']
        else:
            st.error(f"{label}의 데이터를 가져오는 데 실패했습니다. 😞")
            return
    
    # DataFrame으로 변환
    combined_df = pd.DataFrame(all_data)

    # Altair로 차트 생성
    chart = alt.Chart(combined_df.reset_index()).transform_fold(
        [col for col in combined_df.columns],
        as_=['지수', 'KRW']
    ).mark_line().encode(
        x='날짜:T',
        y='KRW:Q',
        color='지수:N'
    ).properties(
        title="KOSPI, KOSDAQ, NASDAQ, S&P 500"
    )

    st.altair_chart(chart, use_container_width=True)

# 시각화 함수 실행
def visualization_function_sub2():
    # Streamlit 앱 시작
    st.title("🌍 글로벌 주식 시장 차트 ")

    # 각 지수와 기간에 따른 API URL 정의
    api_urls = {
        "KOSPI": {
            "3개월": "https://api.stock.naver.com/chart/domestic/index/KOSPI?periodType=month&range=3",
            "1년": "https://api.stock.naver.com/chart/domestic/index/KOSPI?periodType=month&range=12",
            "3년": "https://api.stock.naver.com/chart/domestic/index/KOSPI?periodType=year&range=3",
            "10년": "https://api.stock.naver.com/chart/domestic/index/KOSPI?periodType=year&range=10"
        },
        "KOSDAQ": {
            "3개월": "https://api.stock.naver.com/chart/domestic/index/KOSDAQ?periodType=month&range=3",
            "1년": "https://api.stock.naver.com/chart/domestic/index/KOSDAQ?periodType=month&range=12",
            "3년": "https://api.stock.naver.com/chart/domestic/index/KOSDAQ?periodType=year&range=3",
            "10년": "https://api.stock.naver.com/chart/domestic/index/KOSDAQ?periodType=year&range=10"
        },
        "NASDAQ": {
            "3개월": "https://api.stock.naver.com/chart/foreign/index/.IXIC?periodType=month&range=3",
            "1년": "https://api.stock.naver.com/chart/foreign/index/.IXIC?periodType=month&range=12",
            "3년": "https://api.stock.naver.com/chart/foreign/index/.IXIC?periodType=year&range=3",
            "10년": "https://api.stock.naver.com/chart/foreign/index/.IXIC?periodType=year&range=10"
        },
        "S&P 500": {
            "3개월": "https://api.stock.naver.com/chart/foreign/index/.INX?periodType=month&range=3",
            "1년": "https://api.stock.naver.com/chart/foreign/index/.INX?periodType=month&range=12",
            "3년": "https://api.stock.naver.com/chart/foreign/index/.INX?periodType=year&range=3",
            "10년": "https://api.stock.naver.com/chart/foreign/index/.INX?periodType=year&range=10"
        }
    }

    # Sidebar에 체크박스로 지수 선택
    st.sidebar.subheader("📊 표시할 지수 선택")
    show_kospi = st.sidebar.checkbox("KOSPI", value=True)
    show_kosdaq = st.sidebar.checkbox("KOSDAQ", value=True)
    show_nasdaq = st.sidebar.checkbox("NASDAQ")
    show_sp500 = st.sidebar.checkbox("S&P 500")

    # 라디오 버튼을 가로로 표시 (기본값을 "10년"으로 설정)
    time_periods = ["3개월", "1년", "3년", "10년"]
    selected_period = st.sidebar.radio(
        "⏳ 기간 선택",
        time_periods,
        index=3,  # 기본값으로 "10년" 선택
        horizontal=True  # Streamlit의 기본 옵션
    )

    # 선택된 지수만큼 데이터 합쳐서 표시
    selected_indices = {}
    if show_kospi:
        selected_indices["KOSPI"] = api_urls["KOSPI"]
    if show_kosdaq:
        selected_indices["KOSDAQ"] = api_urls["KOSDAQ"]
    if show_nasdaq:
        selected_indices["NASDAQ"] = api_urls["NASDAQ"]
    if show_sp500:
        selected_indices["S&P 500"] = api_urls["S&P 500"]

    # 차트를 하나로 합쳐서 표시
    if selected_indices:
        display_combined_chart(selected_indices, selected_period)
    else:
        st.error("🚨 표시할 지수를 최소한 하나 선택해주세요.")

if __name__ == "__main__":
    visualization_function_sub2()
