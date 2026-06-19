import streamlit as st
import random

st.set_page_config(page_title="🐤 병아리 위젯 놀이터", page_icon="🐤", layout="centered")
st.title("🐤 병아리 위젯 놀이터")
st.write("아래 부품들을 직접 만져 보세요. 만지는 순간 화면이 살아 움직여요!")

# 1. 이미지
st.image("병아리.jpg")

# 2. 슬라이더 — 즉각 반응
나이 = st.slider("🎂 나이를 골라 보세요", 0, 100, 15)
st.write(f"우와, **{나이}살**이군요!")

# 3. 컬러피커 — 만지면 바로 색이 바뀜
색 = st.color_picker("🎨 좋아하는 색을 골라 보세요", "#FFD400")
st.markdown(f"<h3 style='color:{색}'>이 색이 마음에 드나요?</h3>", unsafe_allow_html=True)

# 4. 선택 상자 + 이모지 반응
간식 = st.selectbox("🍙 오늘의 간식은?", ["김밥", "라면", "떡볶이", "치킨"])
이모지 = {"김밥": "🍙", "라면": "🍜", "떡볶이": "🌶️", "치킨": "🍗"}
st.write(f"좋아요! 오늘은 {이모지[간식]} **{간식}** 입니다.")

# 5. 체크박스 — 조건에 따라 화면 변신
if st.checkbox("✨ 비밀 메시지 열기"):
    st.info("당신은 멋진 개발자가 될 거예요! 🚀")

# 6. 텍스트 입력 — 환영 인사
이름 = st.text_input("✏️ 이름을 적어 주세요")
if 이름:
    st.success(f"{이름}님, 병아리 놀이터에 오신 걸 환영해요! 🐤")

st.divider()

# 7. 버튼 — 누르면 행운 + 풍선
if st.button("🎉 오늘의 행운 뽑기"):
    행운 = random.choice([
        "오늘은 좋은 일이 생길 거예요! 🍀",
        "용기를 내면 멋진 하루가 돼요! 💪",
        "작은 도전이 큰 변화를 만들어요! ⭐",
        "웃는 얼굴엔 복이 와요! 😊",
    ])
    st.metric("🔮 행운 지수", f"{random.randint(80, 100)}점", f"+{random.randint(1, 20)}")
    st.write(행운)
    st.balloons()
