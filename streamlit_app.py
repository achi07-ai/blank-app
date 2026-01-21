import streamlit as st
import random
import time

# ページの設定
st.set_page_config(page_title="箱当てチャレンジ", page_icon="🎁", layout="centered")

# カスタムCSSで見た目をリッチに
st.markdown("""
    <style>
    .stButton>button {
        height: 150px;
        font-size: 50px !important;
        border-radius: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        border-color: #FF4B4B;
    }
    .score-text {
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)

# セッション状態の初期化
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'high_score' not in st.session_state:
    st.session_state.high_score = 0
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 3)
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'last_result' not in st.session_state:
    st.session_state.last_result = ""

def check_answer(box_number):
    if box_number == st.session_state.target:
        st.session_state.score += 1
        st.session_state.target = random.randint(1, 3)
        st.session_state.last_result = "success"
        if st.session_state.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.score
    else:
        st.session_state.game_over = True

# --- メインUI ---
st.title("🎁 究極の箱当てチャレンジ")
st.write("### 運を味方につけて、連続正解を目指せ！")

# スコア表示エリア
col_s1, col_s2 = st.columns(2)
col_s1.metric("現在のスコア", f"{st.session_state.score} 回")
col_s2.metric("自己ベスト", f"{st.session_state.high_score} 回")

# プログレスバー（目標10連勝！）
progress = min(st.session_state.score * 10, 100)
st.progress(progress, text=f"目標まで: {st.session_state.score}/10")

st.divider()

if st.session_state.game_over:
    st.error(f"## ❌ 終了！")
    st.write(f"### 今回の記録: {st.session_state.score}回")
    
    if st.session_state.score == st.session_state.high_score and st.session_state.score > 0:
        st.warning("✨ 新記録達成！おめでとう！ ✨")
        
    if st.button("🔥 もう一度リベンジする", use_container_width=True):
        st.session_state.score = 0
        st.session_state.target = random.randint(1, 3)
        st.session_state.game_over = False
        st.rerun()

else:
    # 前回の結果に応じた演出
    if st.session_state.last_result == "success":
        st.balloons()
        st.success("🎉 正解！継続中！")
        st.session_state.last_result = ""

    st.write("#### 好きな箱をタップしてください：")
    cols = st.columns(3)
    boxes = ["📦", "🎁", "🗳️"] # 遊び心のあるアイコン
    
    for i, col in enumerate(cols):
        with col:
            if st.button(f"{boxes[i]}\n\n{i+1}", key=f"box_{i+1}", use_container_width=True):
                check_answer(i+1)
                st.rerun()

    st.info("ヒント：当たりは常に移動しています...")

# フッター
st.markdown("---")
st.caption("Produced by Streamlit Game Engine")
