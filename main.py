import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🎯 MBTI 진로 추천", 
    page_icon="🚀", 
    layout="centered",
)

# 타이틀
st.markdown(
    "<h1 style='text-align: center; color: #4B0082;'>✨ 나만의 MBTI 진로 추천 🚀</h1>", 
    unsafe_allow_html=True
)
st.write("당신의 MBTI 유형을 선택하면, 그에 어울리는 직업을 추천해드립니다! 🎉")

# 사이드바
st.sidebar.header("🔍 MBTI 진로 추천")
st.sidebar.markdown("본 사이트는 MBTI 유형별로 어울리는 직업을 추천해주는 진로 교육용 웹앱입니다.")

# MBTI 리스트 및 직업 매핑
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]
career_recommendations = {
    "ISTJ": ["보험 계리사 📊", "회계사 💼", "프로젝트 매니저 📋"],
    "ISFJ": ["사회복지사 🤝", "교사 🍎", "간호사 🏥"],
    "INFJ": ["심리 상담가 🧠", "작가 ✍️", "전략 기획자 🎯"],
    "INTJ": ["연구원 🔬", "데이터 과학자 📈", "전략 컨설턴트 🧩"],
    "ISTP": ["엔지니어 ⚙️", "그래픽 디자이너 🎨", "기계공학자 🏗️"],
    "ISFP": ["디자이너 🎨", "사진작가 📷", "영상 편집가 🎬"],
    "INFP": ["작가 ✍️", "컨텐츠 크리에이터 🎥", "상담 심리사 💬"],
    "INTP": ["소프트웨어 개발자 💻", "데이터 분석가 📊", "학자 🎓"],
    "ESTP": ["영업 전문가 📞", "이벤트 기획자 🎉", "파일럿 ✈️"],
    "ESFP": ["연예인 🎤", "댄스 강사 💃", "이벤트 호스트 🎈"],
    "ENFP": ["마케팅 전문가 📣", "HR 전문가 👥", "창업가 🚀"],
    "ENTP": ["분석 컨설턴트 📑", "발명가 💡", "스타트업 창업가 🌟"],
    "ESTJ": ["관리자 🗂️", "운영 책임자 🔧", "검사 ⚖️"],
    "ESFJ": ["교사 🍎", "HR 매니저 👫", "간호 관리자 🏥"],
    "ENFJ": ["리더십 코치 💼", "강사 🎤", "커뮤니티 매니저 🌍"],
    "ENTJ": ["CEO 🏢", "경영 컨설턴트 📈", "프로젝트 리더 🏆"],
}

# 사용자 선택
selected_mbti = st.selectbox("🔮 MBTI를 선택하세요", mbti_list)

# 추천 버튼 및 결과
if st.button("💡 추천받기"):
    recs = career_recommendations.get(selected_mbti, [])
    if recs:
        st.markdown("<h3 style='color: #FF4500;'>🎉 추천 직업 목록:</h3>", unsafe_allow_html=True)
        for job in recs:
            emoji = random.choice(["💖", "⭐", "🔥", "🎯"])
            st.markdown(f"- {job} {emoji}")
        st.balloons()
    else:
        st.warning("😢 추천할 직업이 없어요...")

# 하단 푸터
st.markdown("---")
st.markdown("<div style='text-align: center; color: #888888;'>© 2025 MBTI 진로 추천 사이트</div>", unsafe_allow_html=True)
