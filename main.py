import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

# 2. 고급스러운 다크 모드 커스텀 CSS 스타일링
st.markdown("""
<style>
    /* 전체 배경 및 기본 텍스트 */
    .stApp {
        background-color: #12161A;
        color: #E2E8F0;
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }
    
    /* 상단 헤더 컨테이너 */
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #1E2630 0%, #25303D 100%);
        padding: 32px 20px;
        border-radius: 24px;
        border: 2px solid #334155;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.45);
        margin-bottom: 28px;
    }
    .main-header h1 {
        font-size: 2.2rem;
        color: #FCD34D;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .main-header p {
        font-size: 1.1rem;
        color: #94A3B8;
        margin: 0;
        font-weight: 500;
    }

    /* 포켓몬 메인 카드 */
    .poke-card {
        background-color: #1A2026;
        border-radius: 24px;
        padding: 32px 24px;
        box-shadow: 0 16px 32px rgba(0, 0, 0, 0.5);
        border: 2px solid #2E3B4E;
        text-align: center;
        margin-top: 25px;
    }

    /* 상단 MBTI 라벨 */
    .mbti-chip {
        display: inline-block;
        font-size: 1.15rem;
        font-weight: 800;
        color: #FBBF24;
        background: rgba(251, 191, 36, 0.12);
        padding: 6px 18px;
        border-radius: 20px;
        border: 1px solid rgba(251, 191, 36, 0.35);
        margin-bottom: 12px;
    }

    /* 포켓몬 이름 */
    .poke-name {
        font-size: 2.4rem;
        font-weight: 800;
        color: #F8FAFC;
        margin: 10px 0 4px 0;
    }
    .poke-en-name {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 16px;
        font-weight: 600;
    }

    /* 포켓몬 일러스트 배경 후광 효과 */
    .poke-img-wrap {
        display: inline-block;
        padding: 16px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(251, 191, 36, 0.15) 0%, rgba(26, 32, 38, 0) 70%);
        margin-bottom: 15px;
    }
    .poke-img-wrap img {
        filter: drop-shadow(0 12px 20px rgba(0, 0, 0, 0.6));
    }

    /* 타입 뱃지 */
    .type-badge {
        display: inline-block;
        background-color: #242E3B;
        color: #CBD5E1;
        font-size: 1.05rem;
        font-weight: 700;
        padding: 8px 20px;
        border-radius: 20px;
        border: 1px solid #3B4B5E;
        margin-bottom: 22px;
    }

    /* 정보 설명 박스 */
    .desc-box {
        background-color: #202934;
        border-left: 5px solid #F59E0B;
        padding: 18px 20px;
        border-radius: 14px;
        text-align: left;
        margin-top: 14px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .desc-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FCD34D;
        margin-bottom: 6px;
    }
    .desc-content {
        font-size: 1.05rem;
        line-height: 1.65;
        color: #CBD5E1;
        margin: 0;
    }

    /* Streamlit 입력 폼 라벨 색상 */
    div[data-testid="stWidgetLabel"] p {
        color: #CBD5E1 !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
    }

    /* 버튼 스타일 커스텀 */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: #111827;
        font-size: 1.2rem;
        font-weight: 800;
        padding: 12px 24px;
        border-radius: 14px;
        border: none;
        box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);
        width: 100%;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #FBBF24 0%, #F59E0B 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(245, 158, 11, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# 3. 16가지 MBTI 포켓몬 데이터베이스 (PokeAPI 공식 고화질 일러스트 CDN URL 사용)
MBTI_POKEMON_DATA = {
    "ENFP": {
        "kor_name": "이브이",
        "eng_name": "Eevee",
        "type": "노말 ⚪",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "feature": "주변 환경에 따라 무한한 가능성으로 진화하는 팔색조 매력의 포켓몬입니다.",
        "reason": "풍부한 상상력과 어디로 튈지 모르는 열정을 가진 ENFP처럼, 무한한 진화 가능성과 자유로운 에너지를 고스란히 품고 있는 최고의 단짝입니다."
    },
    "ENFJ": {
        "kor_name": "토게키스",
        "eng_name": "Togekiss",
        "type": "페어리 🌸 / 비행 🕊️",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "feature": "다툼을 싫어하고 서로를 아끼는 평화로운 사람들에게 기쁨과 축복을 전해주는 포켓몬입니다.",
        "reason": "타인을 진심으로 응원하고 선한 영향력을 널리 퍼뜨리는 ENFJ의 따뜻한 카리스마와 완벽하게 어우러지는 파트너입니다."
    },
    "ENTP": {
        "kor_name": "팬텀",
        "eng_name": "Gengar",
        "type": "고스트 👻 / 독 ☠️",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "feature": "언제나 장난기 가득한 미소를 띠며 기발하고 예측 불가능한 행동으로 상대를 놀라게 만듭니다.",
        "reason": "재치 있는 논쟁과 번뜩이는 호기심으로 가득 찬 ENTP의 엉뚱하고 유쾌한 두뇌 플레이에 장단을 맞춰줄 찰떡궁합입니다."
    },
    "ENTJ": {
        "kor_name": "루카리오",
        "eng_name": "Lucario",
        "type": "격투 🥊 / 강철 ⚙️",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "feature": "상대의 파동을 감지하고 엄격한 자기 수양과 정의감을 통해 팀을 승리로 이끕니다.",
        "reason": "명확한 비전과 강력한 결단력으로 목표를 향해 달리는 ENTJ의 당당한 리더십을 가장 든든하게 받쳐줍니다."
    },
    "INFP": {
        "kor_name": "치코리타",
        "eng_name": "Chikorita",
        "type": "풀 🍃",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/152.png",
        "feature": "머리의 잎사귀에서 은은하고 달콤한 향기를 풍기며 주변의 지친 마음을 편안하게 치유해 줍니다.",
        "reason": "순수하고 따뜻한 감수성을 지닌 INFP의 마음에 깊은 힐링과 다정한 위로를 건네주는 몽글몽글한 친구입니다."
    },
    "INFJ": {
        "kor_name": "뮤",
        "eng_name": "Mew",
        "type": "에스퍼 🔮",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "feature": "모든 포켓몬의 유전 정보를 가지고 있으며, 맑은 영혼을 가진 존재 앞에만 신비롭게 모습을 드러냅니다.",
        "reason": "깊은 통찰력과 온화함, 그러면서도 신비로운 내면 세계를 간직한 INFJ의 영혼과 깊은 공명을 나눌 수 있습니다."
    },
    "INTP": {
        "kor_name": "후딘",
        "eng_name": "Alakazam",
        "type": "에스퍼 🧠",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "feature": "IQ 5000에 달하는 경이로운 두뇌로 세상의 모든 현상을 분석하고 기억하는 지혜로운 포켓몬입니다
