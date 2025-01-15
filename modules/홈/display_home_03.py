import streamlit as st
import time
def display_home_03():
    """홈 페이지 기본 내용"""
    # 텍스트를 숨기기 위해 empty 사용
    title_placeholder = st.empty()
    description_placeholder = st.empty()
    # 텍스트가 표시되기 전, GIF가 보이도록 처리
    gif_placeholder = st.empty()  # 이곳에 GIF를 표시할 예정입니다.
    gif_placeholder.image("C:/Users/host/Desktop/PROJECT_SeSAC_02/datas/새싹로고(gif).gif", use_column_width=True)
    # GIF가 3초 동안 보이도록 하기
    time.sleep(2.39)
    # GIF가 사라지도록 하기
    gif_placeholder.empty()
    