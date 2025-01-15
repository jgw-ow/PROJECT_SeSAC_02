from modules.크롤링.sub.crawling_function_sub1 import crawling_function_sub1
from modules.크롤링.sub.crawling_function_sub2 import crawling_function_sub2
import streamlit as st

def run_crawling(sub_menu):
    # '결과' 탭을 벗어날 때 상태 초기화
    if sub_menu != "결과":
        # 세션 상태 초기화
        if 'crawling_result' in st.session_state:
            del st.session_state.crawling_result  # 결과 초기화
        if 'category' in st.session_state:
            del st.session_state.category  # 선택한 카테고리 초기화
        if 'max_articles' in st.session_state:
            del st.session_state.max_articles  # 최대 기사 수 초기화

    if sub_menu == "선택":
        # 크롤링 선택 함수 호출
        if crawling_function_sub1():  # 함수에서 True 반환 시
            st.session_state.active_tab = "결과"  # 결과 탭으로 이동

    elif sub_menu == "결과":
        # 결과 탭에서 크롤링 실행
        if 'category' in st.session_state and 'max_articles' in st.session_state:
            # 자동으로 크롤링 실행
            crawling_function_sub2()  # 두 번째 크롤링 함수 호출
        else:
            st.warning("먼저 크롤링 옵션을 선택해 주세요.")