import streamlit as st
import random

# アプリのタイトル
st.title("📦 連続当たり当てゲーム")
st.write("3つの箱の中に1つだけ当たりがあります。外れるまで引き続けよう！")

# セッション状態の初期化（スコアと当たりの位置を保持）
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 3)
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

def check_answer(box_number):
    if box_number == st.session_state.target:
        # 当たりの場合
        st.session_state.score += 1
        st.session_state.target = random.randint(1, 3) # 次の当たりをセット
        st.toast(f"正解！ 現在の記録: {st.session_state.score}回", icon="🎉")
    else:
        # 外れの場合
        st.session_state.game_over = True

# ゲームオーバー画面の表示
if st.session_state.game_over:
    st.error(f"残念！外れです。今回の記録は **{st.session_state.score}** 回でした。")
    if st.button("もう一度挑戦する"):
        st.session_state.score = 0
        st.session_state.target = random.randint(1, 3)
        st.session_state.game_over = False
        st.rerun()

else:
    # 箱の選択ボタンを横に並べる
    st.write(f"### 現在のスコア: **{st.session_state.score}**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("箱 1", use_container_width=True):
            check_answer(1)
            st.rerun()
            
    with col2:
        if st.button("箱 2", use_container_width=True):
            check_answer(2)
            st.rerun()
            
    with col3:
        if st.button("箱 3", use_container_width=True):
            check_answer(3)
            st.rerun()

    st.info("好きな箱をクリックしてください。")
    
