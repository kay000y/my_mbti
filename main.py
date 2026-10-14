import streamlit as st

# 1. 페이지 기본 설정 및 디자인 (따뜻한 크림/노란색 톤, 큰 글씨)
st.set_page_config(
    page_title="MBTI x 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

# 자체 메인 Custom CSS (따뜻한 크림 및 노란색 톤 스타일링)
st.markdown("""
    <style>
    /* 전체 배경색: 따뜻한 크림색 */
    .stApp {
        background-color: #FFFDF0;
        font-family: 'Malgun Gothic', 'Noto Sans KR', sans-serif;
    }
    
    /* 카드 컨테이너 스타일 */
    .pokemon-card {
        background-color: #FFF8DC;
        border: 3px solid #FFE4B5;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(220, 180, 80, 0.2);
        margin-top: 15px;
    }
    
    /* 큰 타이틀 및 텍스트 스타일 */
    .main-title {
        color: #B8860B;
        font-size: 2.3rem !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .sub-title {
        color: #8B6508;
        font-size: 1.2rem !important;
        text-align: center;
        margin-bottom: 25px;
    }
    
    .pokemon-name {
        font-size: 2rem !important;
        font-weight: bold;
        color: #8B4513;
        margin-top: 10px;
    }
    
    .badge-type {
        display: inline-block;
        background-color: #FFD700;
        color: #5C4033;
        font-weight: bold;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 1.1rem;
        margin: 10px 0;
    }
    
    .reason-box {
        background-color: #FFFFFF;
        border-left: 5px solid #FFA500;
        border-radius: 8px;
        padding: 15px;
        text-align: left;
        margin-top: 15px;
        color: #333333;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 16가지 MBTI별 포켓몬 데이터베이스
POKEMON_DATA = {
    "ISTJ": {
        "kor": "거북왕", "eng": "Blastoise", "id": 9, "type": "물",
        "desc": "묵묵하고 침착하게 맡은 임무를 완수하는 든든한 등껍질 포켓몬.",
        "reason": "원칙을 중요시하고 침착한 ISTJ에게 거북왕은 가장 신뢰할 수 있는 단짝입니다. 흔들리지 않는 굳건함으로 서로를 완벽하게 뒷받침해 줍니다."
    },
    "ISFJ": {
        "kor": "해피너스", "eng": "Blissey", "id": 242, "type": "노멀",
        "desc": "상처받은 이를 다정하게 보살피는 헌신과 사랑의 포켓몬.",
        "reason": "주변 사람들을 세심하게 챙기는 ISFJ의 따뜻함과 해피너스의 헌신적인 성향이 깊은 공감대를 형성합니다. 함께 있으면 온세상이 평화로워집니다."
    },
    "INFJ": {
        "kor": "가디안", "eng": "Gardevoir", "id": 282, "type": "초능력 / 페어리",
        "desc": "트레이너와의 깊은 유대를 바탕으로 미래를 예지하고 지키는 포켓몬.",
        "reason": "통찰력이 깊고 이상주의적인 INFJ에게 가디안은 말하지 않아도 마음을 읽는 통하는 영혼의 단짝입니다."
    },
    "INTJ": {
        "kor": "후딘", "eng": "Alakazam", "id": 65, "type": "초능력",
        "desc": "IQ 5000 이상의 놀라운 두뇌로 철저한 전략을 세우는 포켓몬.",
        "reason": "전략적이고 지적인 INTJ와 후딘은 비전을 공유하는 최고의 지략가 콤비입니다. 복잡한 문제를 명쾌하게 해결해 나갑니다."
    },
    "ISTP": {
        "kor": "루카리오", "eng": "Lucario", "id": 448, "type": "강철 / 격투",
        "desc": "상대의 파동을 감지하며 냉철하고 정교하게 행동하는 포켓몬.",
        "reason": "조용하지만 실전에 강하고 문제 해결 능력이 뛰어난 ISTP와 루카리오는 서로의 능력을 높이 평가하는 깔끔하고 멋진 파트너가 됩니다."
    },
    "ISFP": {
        "kor": "메타몽", "eng": "Ditto", "id": 132, "type": "노멀",
        "desc": "상황에 따라 유연하게 변신하며 자유롭게 살아가는 포켓몬.",
        "reason": "자유롭고 유연하며 온화한 ISFP처럼 메타몽 역시 어디서든 자연스럽게 녹아듭니다. 압박감 없이 편안한 일상을 선사합니다."
    },
    "INFP": {
        "kor": "이브이", "eng": "Eevee", "id": 133, "type": "노멀",
        "desc": "무한한 가능성과 풍부한 감성을 품고 있는 진화 포켓몬.",
        "reason": "내면의 열정과 무궁무진한 가능성을 지닌 INFP에게 이브이는 최고의 친구입니다. 어떤 모습으로든 성장할 수 있는 서로의 꿈을 응원합니다."
    },
    "INTP": {
        "kor": "잠만보", "eng": "Snorlax", "id": 143, "type": "노멀",
        "desc": "평소엔 느긋하지만 필요할 때는 놀라운 에너지를 발휘하는 포켓몬.",
        "reason": "생각이 깊고 효율을 중요시하며 느긋한 INTP에게 잠만보는 세상에서 가장 편안한 존재입니다. 함께 여유를 즐기며 호기심을 탐구할 수 있습니다."
    },
    "ESTP": {
        "kor": "피카츄", "eng": "Pikachu", "id": 25, "type": "전기",
        "desc": "통통 튀는 에너지를 발산하며 모험을 즐기는 마스코트 포켓몬.",
        "reason": "스릴과 행동을 좋아하는 ESTP의 에너제틱한 성향과 피카츄의 재기발랄함이 조화를 이룹니다. 어디로 가든 매일이 즐거운 모험이 됩니다."
    },
    "ESFP": {
        "kor": "푸린", "eng": "Jigglypuff", "id": 39, "type": "노멀 / 페어리",
        "desc": "언제 어디서나 무대의 주인공이 되어 노래를 불러주는 포켓몬.",
        "reason": "사람들에게 즐거움을 주는 분위기 메이커 ESFP와 사랑스러운 스타 푸린은 어디서나 주목받는 환상의 콤비입니다."
    },
    "ENFP": {
        "kor": "파이리", "eng": "Charmander", "id": 4, "type": "불꽃",
        "desc": "꼬리의 불꽃처럼 열정과 호기심이 타오르는 포켓몬.",
        "reason": "열정적이고 친근하며 아이디어가 넘치는 ENFP에게 파이리의 끊이지 않는 열정은 아주 매력적입니다. 둘이 함께라면 매일이 시끌벅적 재미있습니다."
    },
    "ENTP": {
        "kor": "팬텀", "eng": "Gengar", "id": 94, "type": "고스트 / 독",
        "desc": "장난기 넘치고 재치 있는 대담함을 가진 유쾌한 포켓몬.",
        "reason": "독창적이고 유쾌한 도전을 즐기는 ENTP에게 팬텀의 창의적인 장난기는 최고의 대화 소재입니다. 지루할 틈이 없는 콤비입니다."
    },
    "ESTJ": {
        "kor": "윈디", "eng": "Arcanine", "id": 59, "type": "불꽃",
        "desc": "당당한 기품과 뛰어난 리더십으로 상대를 압도하는 포켓몬.",
        "reason": "체계적이고 정직하며 리더십이 강한 ESTJ와 충성심 깊고 위풍당당한 윈디는 단단한 신뢰와 책임감으로 묶인 최강의 조합입니다."
    },
    "ESFJ": {
        "kor": "토게피", "eng": "Togepi", "id": 175, "type": "페어리",
        "desc": "주변에 행운과 행복을 가져다주는 밝은 긍정 포켓몬.",
        "reason": "친절하고 타인을 잘 돌보는 ESFJ에게 토게피는 존재만으로도 기쁨을 줍니다. 따뜻한 에너지를 서로 주고받는 밝은 친구가 됩니다."
    },
    "ENFJ": {
        "kor": "망나뇽", "eng": "Dragonite", "id": 149, "type": "드래곤 / 비행",
        "desc": "바다에서 길을 잃은 사람을 돕는 따뜻하고 상냥한 용 포켓몬.",
        "reason": "타인을 이끌고 돕는 따뜻한 리더 ENFJ처럼 망나뇽 또한 상냥함과 강함을 동시에 가졌습니다. 사람들에게 희망을 주는 따뜻한 조력자입니다."
    },
    "ENTJ": {
        "kor": "뮤츠", "eng": "Mewtwo", "id": 150, "type": "초능력",
        "desc": "강력한 의지와 카리스마로 카리스마를 발산하는 전설의 포켓몬.",
        "reason": "높은 목표를 향해 나아가는 대담한 ENFJ/ENTJ의 추진력에 어울리는 강한 파트너입니다. 최고의 자리를 향해 함께 나아갑니다."
    }
}

# 3. 화면 UI 구성
st.markdown('<div class="main-title">⚡ MBTI 단짝 포켓몬 찾기 ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 성격 유형에 딱 맞는 단짝 포켓몬을 만나보세요!</div>', unsafe_allow_html=True)

# MBTI 선택 드롭다운
mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택해 주세요:",
    mbti_list,
    index=0
)

# 검색 버튼
if st.button("✨ 내 단짝 포켓몬 확인하기!", use_container_width=True):
    pokemon = POKEMON_DATA[selected_mbti]
    
    # 4. 축하 효과 (Streamlit 기본 풍선 + JS 폭죽 효과 연출)
    st.balloons()
    
    # 브라우저 JS 폭죽 효과(Canvas Confetti) 
    st.components.v1.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        </script>
    """, height=0)

    # 포켓몬 공식 아트워크 이미지 URL (PokeAPI CDN)
    img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon['id']}.png"

    # 5. 포켓몬 카드 출력
    st.markdown(f"""
        <div class="pokemon-card">
            <div style="font-size: 1.3rem; color: #8B6508;"><b>[{selected_mbti}]</b> 유형의 단짝은 바로...</div>
            <div class="pokemon-name">{pokemon['kor']} <span style="font-size: 1.2rem; color: #A0522D;">({pokemon['eng']})</span></div>
            <div class="badge-type">타입: {pokemon['type']}</div>
            <br/>
            <img src="{img_url}" width="240" style="margin: 15px 0;">
            <div style="font-size: 1.05rem; color: #555;">"{pokemon['desc']}"</div>
            <div class="reason-box">
                💡 <b>어울리는 이유:</b><br/>
                {pokemon['reason']}
            </div>
        </div>
    """, unsafe_allow_html=True)
