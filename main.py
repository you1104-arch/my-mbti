import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

# 2. 따뜻한 크림/노란색 톤의 커스텀 CSS 스타일링
st.markdown("""
<style>
    /* 전체 배경 및 폰트 색상 */
    .stApp {
        background-color: #FFFDF0;
        color: #3E2723;
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }
    
    /* 제목 및 부제목 */
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #FFF3B0 0%, #FFE082 100%);
        padding: 30px 20px;
        border-radius: 24px;
        border: 3px solid #FFE082;
        box-shadow: 0 8px 16px rgba(255, 179, 0, 0.15);
        margin-bottom: 30px;
    }
    .main-header h1 {
        font-size: 2.3rem;
        color: #4E342E;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .main-header p {
        font-size: 1.15rem;
        color: #6D4C41;
        margin: 0;
        font-weight: 500;
    }

    /* 포켓몬 카드 컨테이너 */
    .poke-card {
        background-color: #FFFFFF;
        border-radius: 24px;
        padding: 30px 25px;
        box-shadow: 0 10px 25px rgba(212, 163, 89, 0.2);
        border: 3px solid #FFE57F;
        text-align: center;
        margin-top: 25px;
    }

    /* 포켓몬 이름 */
    .poke-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #3E2723;
        margin: 15px 0 5px 0;
    }
    .poke-en-name {
        font-size: 1.1rem;
        color: #8D6E63;
        margin-bottom: 15px;
        font-weight: 600;
    }

    /* 타입 뱃지 */
    .type-badge {
        display: inline-block;
        background-color: #FFECB3;
        color: #5D4037;
        font-size: 1.05rem;
        font-weight: 700;
        padding: 8px 18px;
        border-radius: 25px;
        border: 2px solid #FFD54F;
        margin-bottom: 20px;
    }

    /* 설명 박스 */
    .desc-box {
        background-color: #FFF9E6;
        border-left: 6px solid #FFCA28;
        padding: 16px 20px;
        border-radius: 12px;
        text-align: left;
        margin-top: 15px;
    }
    .desc-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #4E342E;
        margin-bottom: 6px;
    }
    .desc-content {
        font-size: 1.05rem;
        line-height: 1.65;
        color: #424242;
        margin: 0;
    }

    /* 버튼 스타일 */
    div.stButton > button:first-child {
        background-color: #FFCA28;
        color: #3E2723;
        font-size: 1.25rem;
        font-weight: 700;
        padding: 14px 28px;
        border-radius: 16px;
        border: 2px solid #FFB300;
        box-shadow: 0 4px 10px rgba(255, 179, 0, 0.3);
        width: 100%;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:first-child:hover {
        background-color: #FFC107;
        border-color: #FFA000;
        transform: translateY(-2px);
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
        "kor_name": "알라딘",
        "eng_name": "Alakazam",
        "type": "에스퍼 🧠",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "feature": "IQ 5000에 달하는 경이로운 두뇌로 세상의 모든 현상을 분석하고 기억하는 지혜로운 포켓몬입니다.",
        "reason": "지적 호기심과 분석적 사고를 즐기는 INTP와 함께 밤새 깊은 사색과 흥미로운 이론을 탐구할 최고의 지적 동반자입니다."
    },
    "INTJ": {
        "kor_name": "뮤츠",
        "eng_name": "Mewtwo",
        "type": "에스퍼 🌀",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "feature": "극한의 집중력과 압도적인 힘을 가졌으며, 감정에 휘둘리지 않고 본질을 꿰뚫어 봅니다.",
        "reason": "철저한 전략과 독립적인 사고로 미래를 설계하는 INTJ의 냉철한 이성과 강한 의지를 온전히 이해합니다."
    },
    "ESFP": {
        "kor_name": "피카츄",
        "eng_name": "Pikachu",
        "type": "전기 ⚡",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "feature": "빨간 볼에서 전기를 뿜어내며 언제 어디서나 분위기를 밝고 활기차게 만드는 슈퍼스타입니다.",
        "reason": "존재 자체만으로 파티의 중심이 되고 긍정 에너지를 전파하는 ESFP의 반짝이는 매력과 완벽한 싱크로율을 자랑합니다."
    },
    "ESFJ": {
        "kor_name": "해피너스",
        "eng_name": "Blissey",
        "type": "노말 🥚",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "feature": "행복이 듬뿍 담긴 알을 나누어주며, 슬퍼하거나 아픈 포켓몬을 지극정성으로 보살핍니다.",
        "reason": "주변 사람들을 살뜰히 챙기고 다정다감하게 공동체를 돌보는 ESFJ의 따뜻한 모성애와 꼭 닮았습니다."
    },
    "ESTP": {
        "kor_name": "리자몽",
        "eng_name": "Charizard",
        "type": "불꽃 🔥 / 비행 🐉",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "feature": "강한 상대를 만나면 꼬리의 불꽃이 더욱 뜨겁게 타오르는 승부욕과 용기의 상징입니다.",
        "reason": "스릴 넘치는 도전을 즐기고 뛰어난 순발력으로 현실의 위기를 돌파하는 ESTP의 와일드한 에너지와 가장 잘 어울립니다."
    },
    "ESTJ": {
        "kor_name": "윈디",
        "eng_name": "Arcanine",
        "type": "불꽃 🦁",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "feature": "위풍당당한 자태와 깊은 충성심을 지녔으며, 흔들림 없는 규율과 용기로 주인을 지킵니다.",
        "reason": "강한 책임감과 체계적인 실행력으로 조직을 질서정연하게 이끄는 ESTJ의 듬직하고 믿음직한 페이스메이커입니다."
    },
    "ISFP": {
        "kor_name": "푸린",
        "eng_name": "Jigglypuff",
        "type": "노말 🎵 / 페어리 💖",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "feature": "자신만의 고유한 멜로디로 노래를 부르며 평화롭고 나른한 분위기를 만드는 아티스트 포켓몬입니다.",
        "reason": "여유로운 삶의 아름다움을 음미하고 따뜻한 예술적 감성을 품은 ISFP에게 더없이 사랑스러운 짝꿍입니다."
    },
    "ISFJ": {
        "kor_name": "이상해씨",
        "eng_name": "Bulbasaur",
        "type": "풀 🌱 / 독 🌿",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        "feature": "등의 씨앗에 영양분을 차곡차곡 모으며 언제나 묵묵하고 충직하게 주인의 곁을 지킵니다.",
        "reason": "보이지 않는 곳에서도 헌신하며 한결같은 온기로 사람들을 지켜주는 ISFJ의 든든한 성품을 닮았습니다."
    },
    "ISTP": {
        "kor_name": "개굴닌자",
        "eng_name": "Greninja",
        "type": "물 💧 / 악 🥷",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
        "feature": "물로 만든 수리검을 능숙하게 다루며, 소리 없이 신속하고 정확하게 기술을 구사합니다.",
        "reason": "말보다 행동이 앞서며 뛰어난 도구 활용과 날카로운 관찰력을 가진 쿨한 실전파 ISTP와 환상의 호흡을 자랑합니다."
    },
    "ISTJ": {
        "kor_name": "거북왕",
        "eng_name": "Blastoise",
        "type": "물 🌊",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "feature": "단단한 등껍질로 어떤 충격도 막아내며, 정확한 조준포로 목표를 빈틈없이 완수합니다.",
        "reason": "원칙을 지키며 신중하고 흔들림 없이 책임을 다하는 ISTJ에게 최고의 신뢰와 안정감을 선사합니다."
    }
}

# 4. 상단 헤더 영역
st.markdown("""
<div class="main-header">
    <h1>💛 나의 MBTI 단짝 포켓몬 💛</h1>
    <p>나의 성향과 꼭 닮은 최고의 포켓몬 파트너를 만나보세요!</p>
</div>
""", unsafe_allow_html=True)

# 5. MBTI 선택 및 시작 버튼
col1, col2 = st.columns([2, 1])

with col1:
    mbti_list = list(MBTI_POKEMON_DATA.keys())
    selected_mbti = st.selectbox(
        "✨ 당신의 MBTI 성격 유형을 선택해 주세요:",
        mbti_list,
        index=0
    )

with col2:
    st.write("")  # 수직 여백 맞춤용
    st.write("")
    find_button = st.button("단짝 찾기 🔍")

# 세션 상태로 이전 결과 유지
if "selected" not in st.session_state:
    st.session_state.selected = selected_mbti

if find_button:
    st.session_state.selected = selected_mbti
    # 🎉 축하 화면 효과 (풍선 + 눈꽃 효과)
    st.balloons()

# 6. 결과 화면 렌더링
target = MBTI_POKEMON_DATA[st.session_state.selected]

st.markdown(f"""
<div class="poke-card">
    <div style="font-size: 1.3rem; font-weight: 700; color: #FFA000; letter-spacing: 1px;">
        ★ {st.session_state.selected} 유형의 소울메이트 ★
    </div>
    <div class="poke-name">{target['kor_name']}</div>
    <div class="poke-en-name">({target['eng_name']})</div>
    <img src="{target['img_url']}" width="240" style="margin: 10px auto; filter: drop-shadow(0 6px 10px rgba(0,0,0,0.12));">
    <br>
    <div class="type-badge">타입: {target['type']}</div>
    
    <div class="desc-box">
        <div class="desc-title">🌟 포켓몬 도감 특징</div>
        <p class="desc-content">{target['feature']}</p>
    </div>
    
    <div class="desc-box" style="margin-top: 15px; border-left-color: #FFA000;">
        <div class="desc-title">🤝 단짝으로 어울리는 이유</div>
        <p class="desc-content">{target['reason']}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# 하단 격려 문구
st.markdown("<p style='text-align: center; color: #A1887F; margin-top: 30px; font-size: 0.95rem;'>모험을 떠날 준비가 되셨나요? 언제든 MBTI를 변경하고 새로운 파트너를 만나보세요!</p>", unsafe_allow_html=True)
