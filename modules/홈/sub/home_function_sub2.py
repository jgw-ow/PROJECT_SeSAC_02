import streamlit as st
from PIL import Image


def display_sub2():
    # HOME으로 돌아가는 버튼 추가
    if st.button("🏠HOME"):
        st.session_state.show_home = True  # HOME 페이지 표시
        st.session_state.current_page = "HOME"  # 현재 페이지를 HOME으로 설정
        st.rerun()  # 페이지 새로 고침

    st.title("정윤 페이지ʕ •ᴥ•ʔ")
    st.write("여기는 정윤 페이지입니다.  -ˋˏ ♡ ˎˊ- ")

    # 이미지 경로 설정
    image = Image.open("C:/Users/host/Desktop/PROJECT_SeSAC_02/datas/정윤님.JPG")
    resized_image = image.resize((200, 250))  # 가로 200px, 세로 250px로 조정

    # 이미지 표시
    st.image(resized_image)

    st.write("👩🏻‍💻 : 이번 프로젝트 정말 재밌었어요. 좋은 조원분들을 만나 많은 것을 배웠습니다.")
    st.write("<b>담당 업무</b> : 주요 주가 지수를 시각화했어요", unsafe_allow_html=True)
    st.write("MBTI : INFJ")
    st.write("")