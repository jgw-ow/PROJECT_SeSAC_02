import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# Streamlit 앱 설정
st.set_page_config(page_title="주식 현재가 비교", layout="wide")
st.write("")

# 주식 데이터 크롤링 함수
def extract_stock_data(tag):
    tds = tag.select('td')
    return {
        "순위": tds[0].text.strip(),
        "종목명": tds[1].text.strip(),
        "현재가": tds[2].text.strip().replace(',', ''),  # 쉼표 제거
        "등락률": tds[4].text.strip(),
        "거래량": tds[5].text.strip().replace(',', '')  # 거래량
    }

def fetch_stock_data():
    url = 'https://finance.naver.com/sise/sise_quant.naver'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stock_data = [
        extract_stock_data(tag)
        for tag in soup.select('table.type_2 tr')
        if len(tag.select('td')) >= 12
    ]
    return stock_data

# 등락률을 숫자형으로 변환 (부호 포함)
def convert_percentage(value):
    try:
        return float(value.replace('%', '').replace(',', '').strip())
    except ValueError:
        return 0.0

def visualization_function_sub1():
    st.title("📈 주식 현재가 비교")

    # 데이터 가져오기
    stocks = fetch_stock_data()
    df = pd.DataFrame(stocks).dropna()
    df['현재가'] = pd.to_numeric(df['현재가'], errors='coerce')
    df['거래량'] = pd.to_numeric(df['거래량'], errors='coerce')
    df['등락률'] = df['등락률'].apply(convert_percentage)  # 등락률을 숫자형으로 변환

    # 기본적으로 상위 10개 종목 표시
    top_10_stocks = df.head(10)
    
    # 사용자 선택 인터페이스 (검색 가능)
    selected_stocks = st.sidebar.multiselect(
        "🔍비교할 주식 선택",
        options=df['종목명'],
        default=top_10_stocks['종목명'],  # 기본적으로 상위 10개 종목 선택
        help="종목명을 검색하여 선택해주세요."  # 사용자에게 검색 기능을 안내
    )

    # 선택된 주식 데이터 필터링 (최대 10개 종목만 필터링)
    filtered_df = df[df['종목명'].isin(selected_stocks)].head(10)

    # 순위 컬럼을 숫자형으로 변환한 뒤 순위로 정렬
    filtered_df['순위'] = pd.to_numeric(filtered_df['순위'], errors='coerce')
    filtered_df = filtered_df.sort_values(by=['순위'])

    # 테이블 출력 (선택된 주식 정보)
    if not filtered_df.empty:
        st.subheader("📋 선택한 주식 데이터")
        filtered_df = filtered_df[['순위', '종목명', '현재가', '등락률', '거래량']]  # 전일비 제거
        
        # 순위와 종목명 순서대로 정렬
        filtered_df_display = filtered_df.set_index('종목명')  # 종목명을 인덱스로 설정하여 보기 좋게
        st.dataframe(filtered_df_display, use_container_width=True)

        # 기본적으로 상위 10개 종목만 그래프에 표시
        top_10_filtered_df = filtered_df.head(10)

        # Streamlit 기본 bar_chart로 그래프 생성
        st.subheader("📊 주식 현재가 그래프")
        
        # 선택된 종목의 '종목명'과 '현재가' 컬럼을 시리즈로 변환
        chart_data = top_10_filtered_df[['종목명', '현재가']].set_index('종목명')
        
        # Streamlit 기본 bar_chart로 막대 그래프 표시
        st.bar_chart(chart_data['현재가'])

    else:
        st.warning("선택된 주식이 없습니다. 주식을 선택해주세요.")

if __name__ == "__main__":
    visualization_function_sub1()
