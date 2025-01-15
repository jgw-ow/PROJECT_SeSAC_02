import streamlit as st
import time

# 카테고리와 그에 해당하는 sid 값 설정
category_sid_map = {
    "정치⚖️": "100",
    "경제💰": "101",
    "사회🏙️": "102",
    "생활/문화🎭": "103",
    "IT/과학👩🏻‍💻": "105",
    "세계🌎": "104"
}

# 크롤링 선택 함수
def crawling_function_sub1():
    # 카테고리 선택
    st.write(' ')
    category = st.selectbox("👉 카테고리 선택", options=list(category_sid_map.keys()))
    st.write(' ')
    # 슬라이더 범위 설정
    max_articles = st.slider("👉 크롤링 기사 수", min_value=1, max_value=200, value=50)  # 기본값은 50

     # 슬라이더 값에 따른 문구 표시
    if max_articles < 50:
        st.warning("❗크롤링 양이 적어 정확도가 떨어질 수 있습니다❗")
    elif 50 <= max_articles < 100:
        st.success("✔️크롤링 양이 적당합니다✔️")
    elif max_articles >= 100:
        st.warning("❗크롤링 양이 많아 많은 시간이 소요됩니다❗")

     # 제출 버튼
    if st.button("Submit"):
        st.session_state.category = category  # 선택한 카테고리 저장
        st.session_state.max_articles = max_articles  # 최대 기사 수 저장
        
        # 성공 메시지 표시
        success_message = st.success("결과 탭에서 결과를 확인하세요.")
        
        # 3초 대기
        time.sleep(3)
        
        # 메시지 제거
        success_message.empty()  # 이전 메시지 제거
        
    