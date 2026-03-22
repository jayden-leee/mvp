import streamlit as st
import time

# ==========================================
# 1. 페이지 설정 및 ChatGPT 스타일 CSS
# ==========================================
st.set_page_config(page_title="Opener AI", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    /* 깔끔한 산돌고딕/프리텐다드 계열 폰트 */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif; }
    
    /* Streamlit 기본 UI(헤더, 푸터, 여백) 완벽 제거 */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container { padding-top: 5rem !important; padding-bottom: 6rem !important; }
    
    /* 전체 배경을 깔끔한 흰색으로 */
    .stApp { background-color: #ffffff; }
    
    /* 상단 고정 네비게이션 바 (ChatGPT 느낌) */
    .top-nav {
        position: fixed; top: 0; left: 0; right: 0;
        height: 60px; background-color: #ffffff;
        border-bottom: 1px solid #e5e5e5;
        display: flex; align-items: center; padding: 0 20px;
        z-index: 999; font-weight: 700; font-size: 18px; color: #111;
    }
    
    /* 챗봇 입력창을 화면 하단에 깔끔하게 고정 */
    .stChatInputContainer {
        border-radius: 16px !important;
        border: 1px solid #e5e5e5 !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        background-color: white !important;
    }
    
    /* 메시지 간격 및 투명 배경 */
    .stChatMessage { padding: 1.5rem 0 !important; background-color: transparent !important; border: none !important; }
    
    /* 바이어 추천 결과 카드 스타일 */
    .buyer-card {
        border: 1px solid #e5e5e5; border-radius: 12px; padding: 20px;
        margin: 10px 0; background-color: #f9f9f9; color: #111;
    }
</style>
<div class="top-nav">🌐 Opener AI <span style="font-weight: 400; color: #888; font-size: 14px; margin-left: 10px;">Enterprise Sales Agent</span></div>
""", unsafe_allow_html=True)

# ==========================================
# 2. 상태 관리 (State Machine) 및 로직
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요. B2B 글로벌 세일즈 AI **오프너(Opener)**입니다.\n\n해외 진출을 준비 중이신 **제품이나 서비스**에 대해 간단히 설명해 주시겠어요?"}
    ]
if "phase" not in st.session_state:
    st.session_state.phase = "ask_product" # 흐름: 제품 묻기 -> 국가 묻기 -> 매칭 -> 생성 완료
if "country" not in st.session_state:
    st.session_state.country = ""

# ==========================================
# 3. 채팅 기록 및 동적 UI 렌더링
# ==========================================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        # [핵심] AI가 바이어를 추천하는 단계일 때 챗봇 말풍선 안에 UI를 생성!
        if msg.get("type") == "matching":
            target = st.session_state.country
            
            # 대표님 피드백 반영: 입력한 국가에 따라 내용이 완벽하게 바뀌는 동적 로직
            if "영국" in target:
                b1, b2 = "🇬🇧 Cult Beauty (영국 런던)", "🇬🇧 Space NK (영국 글로벌)"
            elif "미국" in target:
                b1, b2 = "🇺🇸 Sephora US (미국 뉴욕)", "🇺🇸 Ulta Beauty (미국 시카고)"
            elif "일본" in target:
                b1, b2 = "🇯🇵 Cosme Tokyo (일본 도쿄)", "🇯🇵 Don Quijote (일본 전국)"
            else:
                b1, b2 = f"📍 {target} 현지 최고 유통사 A", f"📍 {target} B2B 핵심 벤더 B"
            
            st.markdown(f"<div class='buyer-card'>", unsafe_allow_html=True)
            st.markdown(f"**{target} 시장 바이어 매칭 결과**")
            st.checkbox(f"✅ {b1} - 매칭률 95%", value=True, key=f"b1_{msg['content']}")
            st.checkbox(f"✅ {b2} - 매칭률 88%", value=True, key=f"b2_{msg['content']}")
            
            if st.button("✨ 선택한 바이어에게 맞춤 제안서 생성하기", type="primary", key=f"btn_{msg['content']}"):
                st.session_state.phase = "generating"
                st.rerun()
            st.markdown("
