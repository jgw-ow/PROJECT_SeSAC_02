import streamlit as st
from modules.홈.display_home_01 import display_home_01  # 홈 함수 호출
from modules.홈.display_home_02 import display_home_02  # 홈 함수 호출
from modules.홈.display_home_03 import display_home_03  # 홈 함수 호출
from modules.크롤링.run_crawling import run_crawling  # 크롤링 실행 함수 호출
from modules.시각화.run_visualization import run_visualization  # 시각화 실행 함수 호출

# 세션 상태 초기화
if "show_home" not in st.session_state:
    st.session_state.show_home = True  # 기본적으로 HOME 페이지 표시
if "current_page" not in st.session_state:
    st.session_state.current_page = "HOME"  # 초기 페이지 설정
if "home_initialized" not in st.session_state:
    st.session_state.home_initialized = False  # HOME 초기화 여부 추가

# display_home_03 함수 실행 여부 제어
if not st.session_state.home_initialized:
    display_home_03()  # display_home_03 함수 처음 실행
    st.session_state.home_initialized = True  # 함수 실행 여부 업데이트

# 사이드바 메뉴 설정
st.sidebar.title("🏷️목차")
menu = st.sidebar.selectbox('', ["HOME", "크롤링", "시각화"])  # 라디오 버튼 대신 셀렉트 박스 사용

if menu == "HOME":
    if st.session_state.show_home:
        # HOME으로 돌아올 때 상태 초기화
        st.session_state.show_home = True
        st.session_state.current_page = "HOME"  # HOME 페이지로 초기화
        display_home_01()  # 홈 페이지 표시
        display_home_02()  # 버튼 구성 페이지 표시
    else:
        # display_home_02 함수에서 현재 페이지를 표시하도록 처리
        display_home_02(show_home=False)  # show_home=False로 전달
        # HOME으로 돌아올 때 상태 초기화
        st.session_state.show_home = True
        st.session_state.current_page = "HOME"  # HOME 페이지로 초기화



elif menu == "크롤링":
    st.title("📰네이버 뉴스 워드클라우드:cloud:")
    tab1, tab2 = st.tabs(["선택", "결과"])  # 두 개의 탭 생성

    with tab1:
        st.subheader("📌크롤링 옵션📌")
        run_crawling("선택")  # 유형 1 크롤링 실행

    with tab2:
        run_crawling("결과")  # 유형 2 크롤링 실행



elif menu == "시각화":
    st.subheader("📌차트 선택📌")
    visualization_sub_menu = st.selectbox("", ["📈주식 현재가", "🌍글로벌 주식차트", "💲주요 주가 지수","📊시가 총액/주식 거래량"])  # 시각화 유형 선택
    st.write("")
    run_visualization(visualization_sub_menu)  # 선택한 유형에 따라 시각화 실행

