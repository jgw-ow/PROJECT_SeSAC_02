import streamlit as st

def display_sub4():
    # HOME 버튼을 상단에 배치
    if st.button("🏠 HOME", key="home_button"):
        st.session_state.show_home = True  # HOME 페이지 표시
        st.session_state.current_page = "HOME"  # 현재 페이지를 HOME으로 설정
        st.rerun()  # 페이지 새로 고침

    # 제목 스타일링
    st.title("🤖 **Profile**")
    st.markdown("<hr>", unsafe_allow_html=True)  # 구분선 추가

    # 스타일을 사용하여 이미지를 원형으로 만들고, 그림자 효과 추가
    st.markdown(
        """
        <style>
        .profile-img {
            border-radius: 50%;
            width: 300px;
            height: 300px;
            object-fit: cover;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);  # 그림자 효과 추가
        }
        .profile-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .profile-text {
            font-size: 18px;
            line-height: 1.6;
            color: #333;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # 이미지와 자기소개 내용의 배치
    col1, col2 = st.columns([1, 2])
    
    # 첫 번째 컬럼: 이미지
    with col1:
        st.markdown(
            f'<div class="profile-container"><img src="https://flexible.img.hani.co.kr/flexible/normal/970/777/imgdb/resize/2019/0926/00501881_20190926.JPG" class="profile-img" alt="경원"></div>',
            unsafe_allow_html=True
        )

    # 두 번째 컬럼: 텍스트
    with col2:
        st.markdown("### **전경원**")
        st.markdown("📌**역할**: 팀원")
        st.markdown("📝**담당업무**: 크롤링, 시각화")
        st.markdown("🔎**MBTI**: ISTP")
        st.markdown("📧**GitHub**: [jgw-ow](https://github.com/jgw-ow)")

        st.write("""
        안녕하세요! 저는 **버스 탄 조장팀**의 **팀원**으로서 **뉴스 크롤링**과 **시각화**를 담당하였습니다.
        원하는 카테고리의 뉴스 기사를 크롤링 할 수 있게 프로그램을 하였고, 
        시가총액과 주식거래량을 Pie chart로 시각화하였습니다.
        """)

    # 구분선 추가
    st.markdown("<hr>", unsafe_allow_html=True)
