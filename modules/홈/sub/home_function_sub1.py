import streamlit as st

# 페이지 표시를 위한 상태 초기화
if "current_page" not in st.session_state:
    st.session_state.current_page = "HOME"  # 초기 페이지 설정

def display_sub1():
    """수진 페이지"""
    st.title("SOOJIN ✨")

    # 두 개의 열을 만들어서 왼쪽에 사진, 오른쪽에 텍스트 배치
    col1, col2 = st.columns([1, 2])  # col1은 1, col2는 2의 비율로 크기 조정

    with col1:
        # 로컬 이미지 추가 (이미지 크기를 절반으로 줄임)
        st.image(r"C:/Users/host/Desktop/PROJECT_SeSAC_02/datas/수진님.jpeg", use_column_width=True)

    with col2:
        # 타이핑 애니메이션을 위한 CSS 추가 (기본 폰트 유지)
        typing_effect = """
        <style>
            .typing {
                font-family: sans-serif;  /* 기본 글꼴로 설정 */
                white-space: nowrap;
                overflow: hidden;
                border-right: .15em solid orange;
                width: 0;
                animation: typing 3s steps(30) 1s 1 normal both, blinkCaret 0.75s step-end infinite;
            }

            @keyframes typing {
                from { width: 0; }
                to { width: 30ch; }
            }

            @keyframes blinkCaret {
                50% { border-color: transparent; }
            }
        </style>
        """
        st.markdown(typing_effect, unsafe_allow_html=True)
        
        # 타이핑 애니메이션 적용된 텍스트
        st.markdown('<p class="typing">안녕하세요, 잘 부탁드립니다! 😊</p>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(""" 
        ### ⭐️ 소개
        - **MBTI**: ISTJ
        - **맡은 업무**: LDA, 주식 현재가 시각화
        - **취미**: 여행, 공연 관람
        - **특기**: 데이터 분석, Python 코딩...이고 싶다
        """)

def display_home():
    """홈 페이지"""
    st.title("홈 페이지")

# 페이지 라우팅
def run_app():
    """앱 실행"""
    # 현재 페이지에 따라 콘텐츠 표시
    if st.session_state.current_page == "HOME":
        display_home()
    elif st.session_state.current_page == "수진 페이지":
        display_sub1()

    # HOME 버튼을 항상 표시하도록 수정
    st.markdown("<div style='margin-top: 40px; text-align: center;'>", unsafe_allow_html=True)
    if st.button("🏠 HOME"):
        st.session_state.current_page = "HOME"  # 현재 페이지를 HOME으로 설정
        st.experimental_rerun()  # 페이지 새로 고침
    st.markdown("</div>", unsafe_allow_html=True)

# 앱 실행
run_app()
