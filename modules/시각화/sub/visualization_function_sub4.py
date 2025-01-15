import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go


def fetch_stock_data():
    """네이버 금융에서 주식 데이터를 크롤링합니다."""
    url = 'https://finance.naver.com/sise/sise_quant.nhn'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    def extract_stock_data(tag):
        """tr 태그에서 데이터 추출"""
        tds = tag.select('td')
        return {
            "종목": tds[1].text.strip(),
            "거래량": tds[5].text.strip(),
            "시가총액": tds[9].text.strip()
        }

    stock = [
        extract_stock_data(tag)
        for tag in soup.select('table.type_2 tr')
        if len(tag.select('td')) == 12
    ]
    return stock


def preprocess_stock_data(stock_data):
    """데이터를 숫자로 변환"""
    for stock in stock_data:
        stock["거래량"] = int(stock["거래량"].replace(',', '').replace('-', '0'))
        stock["시가총액"] = int(stock["시가총액"].replace(',', '').replace('-', '0'))
    return stock_data


def visualization_function_sub4():
    """Streamlit 기반 데이터 시각화"""
    # 데이터 크롤링 및 전처리
    raw_data = fetch_stock_data()
    processed_data = preprocess_stock_data(raw_data)

    # 상위 10개 데이터 추출
    top_10_by_market_cap = sorted(processed_data, key=lambda x: x["시가총액"], reverse=True)[:10]
    top_10_by_volume = sorted(processed_data, key=lambda x: x["거래량"], reverse=True)[:10]

    # 사이드바에서 데이터 유형 선택
    st.sidebar.write('')
    st.sidebar.title("ℹ️ 데이터 유형 선택")
    if st.sidebar.button("시가총액"):
        st.session_state.data_type = "시가총액"
    if st.sidebar.button("주식거래량"):
        st.session_state.data_type = "주식거래량"

    # 기본값 설정
    if 'data_type' not in st.session_state:
        st.session_state.data_type = "시가총액"  # 기본값

    data_type = st.session_state.data_type

    if data_type == "시가총액":
        st.sidebar.write('')
        st.subheader("📊상위 10위 종목 시가총액 데이터")
        market_cap_df = pd.DataFrame(top_10_by_market_cap).drop(columns=["거래량"])
        market_cap_df.index = range(1, len(market_cap_df) + 1)
        st.table(market_cap_df)

        # Plotly 파이 차트 시각화
        st.subheader("🔢상위 10위 시가총액 비율")
        labels = market_cap_df["종목"]
        sizes = market_cap_df["시가총액"]

        # Plotly 파이 차트 설정
        fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=0.3, textinfo='percent+label',
                                       marker=dict(colors=sns.color_palette("husl", len(labels)).as_hex()))])

        # 레이아웃 설정
        fig.update_layout(
            title="상위 10위 시가총액 비율",
            title_x=0.5,
            font=dict(family="NanumGothic", size=12, color="black"),
            showlegend=True,
            width=800,  # 차트 너비
            height=600,  # 차트 높이
            # 파이 차트 안쪽 텍스트 글꼴 두껍게 설정
            annotations=[dict(
                font=dict(size=20, weight='bold'),
                showarrow=False,
                text='시가총액',
                x=0.5,
                y=0.5
            )]
        )

        # Streamlit에서 Plotly 차트 표시
        st.plotly_chart(fig)

    if data_type == "주식거래량":
        st.sidebar.write('')
        st.subheader("📊상위 10위 종목 거래량 데이터")
        volume_df = pd.DataFrame(top_10_by_volume).drop(columns=["시가총액"])
        volume_df.index = range(1, len(volume_df) + 1)
        st.table(volume_df)

        # Plotly 파이 차트 시각화
        st.subheader("🔢상위 10위 거래량 비율")
        labels = volume_df["종목"]
        sizes = volume_df["거래량"]

        # Plotly 파이 차트 설정
        fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=0.3, textinfo='percent+label',
                                       marker=dict(colors=sns.color_palette("husl", len(labels)).as_hex()))])

        # 레이아웃 설정
        fig.update_layout(
            title="상위 10위 거래량 비율",
            title_x=0.5,
            font=dict(family="NanumGothic", size=12, color="black"),
            showlegend=True,
            width=800,  # 차트 너비
            height=600,  # 차트 높이
            # 파이 차트 안쪽 텍스트 글꼴 두껍게 설정
            annotations=[dict(
                font=dict(size=20, weight='bold'),
                showarrow=False,
                text='거래량',
                x=0.5,
                y=0.5
            )]
        )

        # Streamlit에서 Plotly 차트 표시
        st.plotly_chart(fig)
