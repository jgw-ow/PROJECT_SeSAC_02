import streamlit as st
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd

# 한글 폰트 설정 (전역)
plt.rc('font', family='NanumGothic')  # For Windows
# 마이너스 폰트 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# URL 요청 및 BeautifulSoup 객체 생성
def fetch_stock_data():
    url = 'https://finance.naver.com/sise/sise_quant.nhn'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    def extract_stock_data(tag):
        """하나의 tr 태그에서 데이터를 추출"""
        tds = tag.select('td')
        return {
            "종목": tds[1].text.strip(),
            "거래량": tds[5].text.strip(),
            "시가총액": tds[9].text.strip()
        }

    # 유효한 tr 태그를 필터링하여 데이터 수집
    stock = [
        extract_stock_data(tag)
        for tag in soup.select('table.type_2 tr')
        if len(tag.select('td')) == 12
    ]

    return stock

# 데이터 전처리
def preprocess_stock_data(stock_data):
    """거래량과 시가총액 데이터를 숫자로 변환"""
    for stock in stock_data:
        stock["거래량"] = int(stock["거래량"].replace(',', '').replace('-', '0'))
        stock["시가총액"] = int(stock["시가총액"].replace(',', '').replace('-', '0'))
    return stock_data

# 데이터 크롤링 및 전처리
raw_data = fetch_stock_data()
processed_data = preprocess_stock_data(raw_data)

# 상위 10개 데이터 추출
top_10_by_market_cap = sorted(processed_data, key=lambda x: x["시가총액"], reverse=True)[:10]
top_10_by_volume = sorted(processed_data, key=lambda x: x["거래량"], reverse=True)[:10]

# 사용자 선택
st.sidebar.header("분석 옵션")
option = st.sidebar.selectbox("분석할 데이터 선택", ["시가총액", "거래량"])

if option == "시가총액":
    st.subheader("상위 10위 종목 시가총액 데이터")
    # 시가총액 데이터만 출력
    market_cap_df = pd.DataFrame(top_10_by_market_cap)
    market_cap_df = market_cap_df.drop(columns=["거래량"])  # 거래량 열 제외
    market_cap_df.index = range(1, len(market_cap_df) + 1)  # 인덱스를 1부터 시작
    st.write(market_cap_df)

    # 파이 차트로 시각화
    st.subheader("상위 10위 시가총액 파이 차트")
    labels = market_cap_df["종목"]
    sizes = market_cap_df["시가총액"]
    
    # 예쁜 색상 리스트
    colors = plt.cm.Paired(range(len(labels)))

    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
                                      colors=colors, wedgeprops={'edgecolor': 'white'}, pctdistance=0.85)

    # 비율 글씨 스타일 조정
    for autotext in autotexts:
        autotext.set_fontsize(9)  # 글씨 크기 증가
        autotext.set_color('black')  # 글씨 색상 변경
        autotext.set_fontweight('bold')  # 글씨 굵기 설정

    # 텍스트 스타일 조정
    for text in texts:
        text.set_fontsize(10)  # 글씨 크기 증가
        text.set_fontweight('bold')  # 글씨 굵기 설정

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

elif option == "거래량":
    st.subheader("상위 10위 종목 거래량 데이터")
    # 거래량 데이터만 출력
    volume_df = pd.DataFrame(top_10_by_volume)
    volume_df = volume_df.drop(columns=["시가총액"])  # 시가총액 열 제외
    volume_df.index = range(1, len(volume_df) + 1)  # 인덱스를 1부터 시작
    st.write(volume_df)

    # 파이 차트로 시각화
    st.subheader("상위 10위 거래량 파이 차트")
    labels = volume_df["종목"]
    sizes = volume_df["거래량"]
    
    # 예쁜 색상 리스트
    colors = plt.cm.Paired(range(len(labels)))

    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
                                      colors=colors, wedgeprops={'edgecolor': 'white'}, pctdistance=0.85)

    # 비율 글씨 스타일 조정
    for autotext in autotexts:
        autotext.set_fontsize(9)  # 글씨 크기 증가
        autotext.set_color('black')  # 글씨 색상 변경
        autotext.set_fontweight('bold')  # 글씨 굵기 설정

    # 텍스트 스타일 조정
    for text in texts:
        text.set_fontsize(10)  # 글씨 크기 증가
        text.set_fontweight('bold')  # 글씨 굵기 설정

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
