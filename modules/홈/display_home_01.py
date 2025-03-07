import streamlit as st

def display_home_01():
    """홈 페이지 기본 내용"""
    st.title("🌟 5조: 버스 탄 조장 🌟")
    
    # 프로젝트 소개 제목 크기 키우기
    st.header("📊 프로젝트 소개")

    # 항목별 스타일 추가 (번호 매기기 및 아이콘 포함)
    st.write(" ")
    st.markdown("**1️⃣ 네이버 뉴스 크롤링 및 LDA 토픽 모델링**")
    st.write("👉 사용자가 선택한 네이버 뉴스 카테고리에서 최신 기사를 크롤링하여 토픽 모델링을 수행하고, 그 결과를 **워드 클라우드**로 시각화합니다.")
    st.subheader(" ")
    st.markdown("**2️⃣ 주식 데이터 시각화**")
    st.write("📌  **주식 현재가 차트**")
    st.write("📌  **글로벌 주식차트**")
    st.write("📌  **주요 주가지수**")
    st.write("📌  **시가총액과 주식거래량**")
    st.write("👉 크롤링한 실시간 주식 데이터를 차트 형태로 시각화하여, 유의미한 정보를 직관적으로 제공합니다.")

