import streamlit as st

def display_home_02(show_home=True):
    st.sidebar.title("💼팀원")

    # 페이지 전환을 위한 버튼
    if st.sidebar.button('👧🏻수진'):
        st.session_state.current_page = "수진"  # 현재 페이지 업데이트
        st.session_state.show_home = False  # HOME 페이지 숨김
        st.rerun()  # 페이지 새로 고침

    if st.sidebar.button('👩🏻정윤'):
        st.session_state.current_page = "정윤"  # 현재 페이지 업데이트
        st.session_state.show_home = False  # HOME 페이지 숨김
        st.rerun()  # 페이지 새로 고침

    if st.sidebar.button('🧑🏻영재'):
        st.session_state.current_page = "영재"  # 현재 페이지 업데이트
        st.session_state.show_home = False  # HOME 페이지 숨김
        st.rerun()  # 페이지 새로 고침

    if st.sidebar.button('👦🏻경원'):
        st.session_state.current_page = "경원"  # 현재 페이지 업데이트
        st.session_state.show_home = False  # HOME 페이지 숨김
        st.rerun()  # 페이지 새로 고침

    # 기본적으로 'HOME' 페이지 내용 표시
    if show_home:
        st.write('')
    else:
        # 선택된 페이지에 따라 해당 내용 표시
        if st.session_state.current_page == "수진":
            from modules.홈.sub.home_function_sub1 import display_sub1
            display_sub1()  # 수진 페이지 표시
        elif st.session_state.current_page == "정윤":
            from modules.홈.sub.home_function_sub2 import display_sub2
            display_sub2()  # 정윤 페이지 표시
        elif st.session_state.current_page == "영재":
            from modules.홈.sub.home_function_sub3 import display_sub3
            display_sub3()  # 영재 페이지 표시
        elif st.session_state.current_page == "경원":
            from modules.홈.sub.home_function_sub4 import display_sub4
            display_sub4()  # 경원 페이지 표시
