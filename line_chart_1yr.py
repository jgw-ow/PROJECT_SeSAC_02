import requests
import pandas as pd
import streamlit as st

increment_normal = st.button("나스닥")
increment_session = st.button("S&P500")
increment_normal = st.button("코스피")
increment_session = st.button("코스닥")

url = "https://api.stock.naver.com/chart/foreign/index/.IXIC?periodType=month&range=12"
response = requests.get(url)
data = response.json()

    # 데이터 유효성 검사
if 'priceInfos' in data:
    price_infos = data['priceInfos']
else:
    st.error(f"Unexpected response structure: {data}")
    st.stop()

# JSON 데이터에서 날짜와 종가 추출
dates = [item['localDate'] for item in price_infos]
prices = [item['closePrice'] for item in price_infos]

# 날짜 형식 변환 및 DataFrame 생성
df = pd.DataFrame({'Date': dates, 'Close Price': prices})
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')  # 날짜 형식 변환
df = df.set_index('Date')  # 인덱스를 날짜로 설정

# 라인 차트 출력
st.title("NASDAQ Line Chart (1 Year)")
st.line_chart(df['Close Price'])






