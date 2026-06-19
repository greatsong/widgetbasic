import streamlit as st
import random
st.set_page_config(page_title="병아리 위젯 놀이터", page_icon="🐤", layout="centered")
st.title("🐤 병아리 위젯 놀이터")
st.image("병아리.jpg", width=300)  # 픽셀 단위로 가로 크기 고정
귀염 = st.slider("🐤 병아리 귀염지수에 투표해 주세요", 0, 100, 80)
st.write(f"이 병아리의 귀염지수는 **{귀염}점**! " + ("💛" * (귀염 // 20 + 1)))
색 = st.color_picker("🎨 병아리에게 입힐 색을 골라 보세요", "#FFD400")
st.markdown(f"<h3 style='color:{색}'>이 색 옷을 입은 병아리, 어때요?</h3>", unsafe_allow_html=True)
간식 = st.selectbox("🍙 병아리에게 줄 간식은?", ["좁쌀", "옥수수", "상추", "물"])
이모지 = {"좁쌀": "🌾", "옥수수": "🌽", "상추": "🥬", "물": "💧"}
st.write(f"냠냠! 병아리가 {이모지[간식]} **{간식}**을(를) 맛있게 먹어요.")
if st.checkbox("✨ 병아리의 비밀 마음 열기"):
    st.info("삐약! 당신이 좋아요! 🐤💛")
이름 = st.text_input("✏️ 병아리에게 이름을 지어 주세요")
st.divider()
if st.button("💌 병아리의 편지 받기"):
    if not 이름:
        st.warning("먼저 병아리에게 이름을 지어 주세요! ✏️")
    else:
        st.metric("🐤 우리 사이 친밀도", f"{random.randint(85, 100)}점", f"+{random.randint(5, 20)}")
        끝인사 = random.choice([
            "오늘도 나를 예뻐해 줘서 고마워! 🍀",
            "우리 오래오래 친구하자, 삐약! 💛",
            "네 덕분에 매일이 행복해! ⭐",
            "다음에 또 놀러 와 줘! 😊",
        ])
        st.write(
            f"💌 **{이름}로부터 온 편지**\n\n"
            f"안녕, 나의 친구야!\n\n"
            f"나에게 **{이름}**(이)라는 예쁜 이름을 지어 줘서 정말 기뻐. "
            f"귀염지수 **{귀염}점**도, {이모지[간식]} {간식} 간식도 고마워!\n\n"
            f"{끝인사}\n\n"
            f"— 삐약삐약, {이름} 올림 🐤"
        )
        st.balloons()
