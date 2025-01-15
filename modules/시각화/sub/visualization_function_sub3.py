import requests
import streamlit as st
import pandas as pd

# 데이터 가져오기 함수
def fetch_realtime_data(api_url):
    """API에서 실시간 데이터를 가져옵니다."""
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"💥 API에서 데이터를 가져오는 데 실패했습니다: {api_url}. 상태 코드: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"❗ 데이터를 가져오는 중 오류 발생: {e}")
        return None

# 데이터를 가져와 화면에 표시하는 함수
def display_index_data(index_name, api_url, chart_url):
    """지수 데이터를 화면에 표시합니다."""
    data = fetch_realtime_data(api_url)
    if data:
        index_data = data.get("datas", [])[0]  # 첫 번째 데이터만 사용
        if index_data:
            # 주요 정보 추출
            stock_name_map = {
                "KOSPI": "📈 코스피",
                "KOSDAQ": "📊 코스닥",
                "S&P 500": "🌎 S&P 500",
                "NASDAQ": "💻 나스닥"
            }
            stock_name = stock_name_map.get(index_name, index_name)
            
            close_price = index_data.get("closePrice", "N/A")
            fluctuations_ratio = index_data.get("fluctuationsRatio", "N/A")
            open_price = index_data.get("openPrice", "N/A")
            high_price = index_data.get("highPrice", "N/A")
            low_price = index_data.get("lowPrice", "N/A")
            trading_volume = index_data.get("accumulatedTradingVolume", "N/A")
            trading_value = index_data.get("accumulatedTradingValue", "N/A")
            market_status = index_data.get("marketStatus", "N/A")
            last_updated = index_data.get("localTradedAt", "N/A")

            # 데이터 표시
            with st.container():
                st.subheader(f"{stock_name}")
                st.metric(label="📉 종가", value=f"{close_price} pt", delta=f"{fluctuations_ratio} %")
                st.write(f"**시장 상태**: {market_status}")
                st.write(f"**최근 업데이트**: {last_updated}")

                # 차트 추가
                st.image(chart_url, use_column_width=True)

                # 추가 정보 테이블
                additional_info = {
                    "📊 시가": open_price,
                    "📈 고가": high_price,
                    "📉 저가": low_price,
                    "💰 거래량": trading_volume,
                    "💵 거래대금": trading_value,
                }
                df = pd.DataFrame(list(additional_info.items()), columns=["항목", "값"])
                
                # 인덱스를 재설정하여 제거 후 출력
                st.table(df)
        else:
            st.error(f"❌ {index_name} 데이터를 가져오는 데 실패했습니다.")
    else:
        st.error(f"❌ {index_name} 데이터를 API에서 가져오는 데 실패했습니다.")

# visualization_function_sub3 함수 정의
def visualization_function_sub3():
    """Streamlit 앱에서 주요 주가 지수를 시각화합니다."""
    st.title("💲 주요 주가 지수")

    # API URL 목록
    api_urls = {
        "KOSPI": "https://polling.finance.naver.com/api/realtime/domestic/index/KOSPI",
        "KOSDAQ": "https://polling.finance.naver.com/api/realtime/domestic/index/KOSDAQ",
        "S&P 500": "https://polling.finance.naver.com/api/realtime/worldstock/index/.INX",
        "NASDAQ": "https://polling.finance.naver.com/api/realtime/worldstock/index/.IXIC"
    }

    # 차트 URL 목록
    chart_urls = {
        "KOSPI": "https://ssl.pstatic.net/imgfinance/chart/mobile/mini/KOSPI_transparent.png?1736819612470",
        "KOSDAQ": "https://ssl.pstatic.net/imgfinance/chart/mobile/mini/KOSDAQ_transparent.png?1736823180000",
        "S&P 500": "https://ssl.pstatic.net/imgfinance/chart/mobile/world/day/.INX_transparent.png?1736754406000",
        "NASDAQ": "https://ssl.pstatic.net/imgfinance/chart/mobile/world/day/.IXIC_transparent.png?1736756159000"
    }

    # 레이아웃: 각 지수를 열(Column)로 배치
    columns = st.columns(len(api_urls))

    # 각 지수별로 데이터 표시
    for col, (index_name, api_url) in zip(columns, api_urls.items()):
        with col:
            display_index_data(index_name, api_url, chart_urls.get(index_name))

if __name__ == "__main__":
    visualization_function_sub3()
