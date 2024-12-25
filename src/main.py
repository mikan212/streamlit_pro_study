import streamlit as st
import page

# ページ作成
st.set_page_config(
    page_title="勉強場所",
    # layout="wide",    # wideにすると横長なレイアウトに
    initial_sidebar_state="expanded"
)

label = ['ホーム', 'C言語', 'Python']
choice = st.sidebar.selectbox('メニュー', label)

match choice:
    case 'ホーム':
        page.home()

    case 'C言語':
        page.c()

    case 'Python':
        page.python()
