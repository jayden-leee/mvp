import streamlit as st
import time

# ==========================================
# 1. 페이지 및 기본 설정 (Toss 스타일 UI)
# ==========================================
st.set_page_config(page_title="Opener - Global Sales AI", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    /* Toss 느낌의 깔끔하고 둥근 폰트 및 UI */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * {font-family: 'Pretendard', sans-serif;}
    
    .stApp {background-color: #f9fafb;}
    
    /* 둥글고 부드러운 카드 스타일 */
    .card {
        background: white; border-radius: 20px; padding: 25px; 
        box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 20px;
        border: 1px solid #f3f4f6;
    }
    
    /* 토스 블루 포인트 컬러 */
    .highlight {color: #3182f6; font-weight: bold;}
    
    /* 진행 상태 바 숨기기 (깔끔함을 위해) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 세션 상태 관리 (에러 방지용)
# ==========================================
if 'step' not in st.session_state:
    st.session_state.step = 1 # 1: 인터뷰, 2: 바이어 매칭, 3: 제안서 생성
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 대표님의 제품을 전 세계에 팔아드릴 AI 파트너 '오프너'입니다. 🎉\n\n오늘 글로벌 바이어에게 제안할 **제품(또는 서비스)은 어떤 것인가요?** 편하게 자랑해주세요!"}
    ]
if 'product_info' not in st.session_state:
    st.session_state.product_info = ""

# ==========================================
# 3. UI 흐름 제어 라우터
# ==========================================
st.markdown("<h2 style='text-align: center; color: #191f28; font-weight: 800; margin-bottom: 30px;'>🌐 Opener <span style='color:#3182f6'>AI</span></h2>", unsafe_allow_html=True)

# ------------------------------------------
# [STEP 1] AI 챗봇 인터뷰 (어떤 제품이든 파악)
# ------------------------------------------
if st.session_state.step == 1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### 💬 1단계: 제품 인터뷰")
    st.caption("AI와 대화하며 제품의 핵심 소구점(USP)을 추출합니다.")
    
    # 기존 대화 내용 출력
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    # 사용자 입력
    if prompt := st.chat_input("예: 20대 타겟의 비건 인증 수분 크림이야. 패키지가 예뻐."):
        # 사용자 메시지 저장 및 출력
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        # AI 응답 (시뮬레이션: 대화가 3번 오가면 자동 분석 완료)
        with st.chat_message("assistant"):
            if len(st.session_state.messages) < 4:
                ai_response = f"아하, '{prompt}'라는 특징이 있군요! 타겟으로 생각하시는 **국가나 특별한 강점**이 더 있을까요?"
                st.write(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                st.write("✨ 제품의 핵심 강점을 모두 파악했습니다! 전 세계에서 핏이 맞는 바이어를 찾아볼까요?")
                st.session_state.product_info = "사용자 입력 기반 추출된 제품 정보 (시뮬레이션)"
                st.session_state.messages.append({"role": "assistant", "content": "분석 완료"})
                
    # 인터뷰 완료 버튼 (클릭 시 Step 2로 이동)
    if len(st.session_state.messages) >= 4:
        if st.button("🚀 바이어 매칭 시작하기", type="primary", use_container_width=True):
            st.session_state.step = 2
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------
# [STEP 2] 바이어 큐레이션 및 선택
# ------------------------------------------
elif st.session_state.step == 2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### 🎯 2단계: 최적 바이어 매칭")
    st.caption("AI가 제품 특성을 분석하여 성공 확률이 높은 바이어를 추천합니다.")
    
    with st.spinner("전 세계 바이어 DB를 검색하고 있습니다... 🌍"):
        time.sleep(1.5) # 검색 로딩 시뮬레이션
        
    st.success("대표님의 제품과 핏이 맞는 바이어 3곳을 찾았습니다!")
    
    st.write("보내고 싶은 바이어를 선택해 주세요.")
    
    # 범용 바이어 Mock Data
    buyer1 = st.checkbox("🇺🇸 **Sephora US (미국)** | Fit: 95점 | '비건/친환경 패키징' 브랜드 소싱 중", value=True)
    buyer2 = st.checkbox("🇯🇵 **Cosme Tokyo (일본)** | Fit: 88점 | '20대 타겟 트렌디 화장품' 관심 높음", value=True)
    buyer3 = st.checkbox("🇬🇧 **Cult Beauty (영국)** | Fit: 82점 | 아시아 뷰티 브랜드 라인업 확장 예정")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ 다시 인터뷰하기", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("✨ 맞춤형 제안서 생성하기", type="primary", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------
# [STEP 3] 초개인화 제안서 생성 및 발송
# ------------------------------------------
elif st.session_state.step == 3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### 📄 3단계: 초개인화 제안서 생성")
    
    # 생성 애니메이션
    progress_text = "바이어별 국가 문화와 톤앤매너를 분석하여 제안서를 작성 중입니다..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()
    
    st.success("✅ 선택한 2개사에 대한 맞춤형 제안서와 메일이 완성되었습니다!")
    st.write("---")
    
    # 결과물 출력 UI (토스 스타일의 아코디언)
    with st.expander("🇺🇸 Sephora US (미국) - 직설적이고 수치 중심의 제안"):
        st.markdown("**[AI 추천 메일 본문]**")
        st.info("Hi Sarah,\n\n최근 Sephora가 비건 뷰티 라인업을 30% 확장한다는 뉴스를 보았습니다. 당사의 제품은 20대 타겟 비건 인증을 완료했으며, 기존 브랜드 대비 리텐션이 20% 높습니다...")
        st.download_button("📄 맞춤형 피치덱 다운로드 (PDF)", data="dummy_pdf_data", file_name="Sephora_Pitch.pdf")

    with st.expander("🇯🇵 Cosme Tokyo (일본) - 격식을 갖춘 디테일 중심의 제안"):
        st.markdown("**[AI 추천 메일 본문]**")
        st.info("야마모토 부장님께,\n\n귀사의 무궁한 발전을 기원합니다. Cosme Tokyo의 최근 20대 트렌드 리포트를 인상 깊게 읽었습니다. 당사는 이에 부합하는 정교한 패키징과 성분 데이터를 보유하고 있으며...")
        st.download_button("📄 맞춤형 피치덱 다운로드 (PDF)", data="dummy_pdf_data", file_name="Cosme_Pitch.pdf")
        
    st.write("")
    if st.button("🚀 연동된 메일로 즉시 발송하기", type="primary", use_container_width=True):
        st.balloons()
        st.toast("성공적으로 메일이 발송되었습니다!", icon="✅")
    st.markdown("</div>", unsafe_allow_html=True)
