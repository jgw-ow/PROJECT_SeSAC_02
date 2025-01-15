import streamlit as st
from PIL import Image

def display_sub3():
    # HOME으로 돌아가는 버튼 추가
    if st.button("🏠 HOME"):
        st.session_state.show_home = True  # HOME 페이지 표시
        st.session_state.current_page = "HOME"  # 현재 페이지를 HOME으로 설정
        st.rerun()  # 페이지 새로 고침

    st.write(" ")
    st.title("영재")

    # 이미지와 자기소개 내용의 배치
    col1, col2 = st.columns([1, 1])  # 두 개의 열 생성

    # 첫 번째 컬럼: 자기소개 내용
    with col1:
        st.write(" ")
        st.write("안녕하세요,,")
        st.write("버스가 편안했습니다,,")
        st.write("시간이 조금 부족해서,,")
        st.write(" ")
        st.write(" ")
        st.write("📌 **역할** : 조장")
        st.write("📝 **담당업무** : 구조 잡기, 크롤링, 승차감 판단하기")
        st.write("🔎 **MBTI** : ESFJ")

    # 두 번째 컬럼: 이미지
    with col2:
        image = Image.open("C:/Users/host/Desktop/PROJECT_SeSAC_02/datas/영재.png")  # 이미지 경로 설정
        resized_image = image.resize((500, 500))  # 이미지 크기 조정 (가로 400px, 세로 400px)
        st.image(resized_image, use_column_width=False)  # 이미지 표시
