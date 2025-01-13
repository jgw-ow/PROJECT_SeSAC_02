import requests
import pandas as pd
import streamlit as st

# 데이터 가져오기 함수
def fetch_data(api_url):
    """API에서 데이터를 가져와 DataFrame으로 변환"""
    response = requests.get(api_url)
    data = response.json()
    if 'priceInfos' in data:
        price_infos = data['priceInfos']
        dates = [item['localDate'] for item in price_infos]
        prices = [item['closePrice'] for item in price_infos]
        df = pd.DataFrame({'Date': dates, 'Close Price': prices})
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
        return df.set_index('Date')
    else:
        return None

# 차트 그리기 함수
def display_chart(title, api_url):
    """차트 데이터를 가져오고 라인 차트를 표시"""
    data = fetch_data(api_url)
    if data is not None:
        st.subheader(title)
        st.line_chart(data['Close Price'])
    else:
        st.error(f"Failed to fetch data for {title}")

# Streamlit 앱
st.title("Global Stock Market Charts")

# 각 지수의 API URL
urls = {
    "KOSPI": "https://api.stock.naver.com/chart/domestic/index/KOSPI?periodType=month&range=12",
    "KOSDAQ": "https://api.stock.naver.com/chart/domestic/index/KOSDAQ?periodType=month&range=12",
    "NASDAQ": "https://api.stock.naver.com/chart/foreign/index/.IXIC?periodType=month&range=12",
    "S&P 500": "https://api.stock.naver.com/chart/foreign/index/.INX?periodType=month&range=12"

}

# 각 버튼 만들기
kospi_button = st.button("Show KOSPI")
kosdaq_button = st.button("Show KOSDAQ")
nasdaq_button = st.button("Show NASDAQ")
sp500_button = st.button("Show S&P 500")

# 버튼 클릭 시 차트 표시
if kospi_button:
    display_chart("KOSPI", urls["KOSPI"])

if kosdaq_button:
    display_chart("KOSDAQ", urls["KOSDAQ"])

if nasdaq_button:
    display_chart("NASDAQ", urls["NASDAQ"])

if sp500_button:
    display_chart("S&P 500", urls["S&P 500"])

