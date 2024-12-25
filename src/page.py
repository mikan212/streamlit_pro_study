import streamlit as st
import requests
import os

WEBHOOK_URL = 'https://discord.com/api/webhooks/1321201577851093085/L_rOzlKIGnjLIufw6SsqjiAoq2I4-uFx4NQ1WeuEGvqPoEkLEVKvp2Zct0T4ktjgCVfv'


def feedback(send_contents, send_img):
    data = {
        "content": send_contents
    }
    files = {
        "file": ("image.png", send_img, "image/png")
    }
    response = requests.post(WEBHOOK_URL, data=data, files=files)

    if response.status_code == 204 or response.status_code == 200:
        st.success("フィードバックを送信しました！ご協力ありがとうございます。")
    else:
        st.error("送信に失敗しました。再度お試しください。")


def clear_text_area():
    st.session_state.text_area_content = ""  # セッションステートをクリア


def home():
    st.header("初心者のためのプログラミング記事", divider="red")
    st.markdown(
        '''
        ##### これからプログラミングを勉強したい方を対象とした記事です。

        この記事は**プログラミングの基礎知識**や**環境構築手順**、\
        それぞれの言語を使たプログラムの書き方などを**豊富なサンプルから学習できる**内容です。\
        プログラミング入門者は是非参考にしてください。
        '''
    )
    container1 = st.container(border=True)
    with container1:
        st.markdown(':red[この記事で学べること]')
        with st.expander('**C言語**'):
            st.markdown(
                '''
                 1. C言語ってどんな言語
                 2. 環境構築
                 3. 変数・データ型
                 4. 演算
                 5. 入出力処理
                 6. コメント
                '''
            )

        with st.expander('**Python3**'):
            st.markdown(
                '''
                 1. Pythonってどんな言語
                 2. 環境構築
                 3. 変数・データ型
                 4. 演算
                 5. 入出力処理
                 6. コメント
                 7. 文字列処理
                 8. 条件分岐
                 9. 反復処理
                10. 関数
                11. オブジェクト指向
                12. モジュール・パッケージ・ライブラリ
                13. 例外処理
                14. 日付・時刻
                15. ファイル・ディレクトリ操作
                16. まとめ

                '''
            )

    st.markdown('---')

    container2 = st.container(border=True)
    with container2:
        st.markdown('##### フィードバックを送信する')
        if "text_area_content" not in st.session_state:
            st.session_state.text_area_content = ""
        st.markdown('###### :red[※個人情報など個人を特定できる情報を含めないでください]')
        st.text_area(
            label="ここにテキストを入力してください",
            value=st.session_state.text_area_content,  # セッションステートの値を使用
            key="text_area_content",
            height=150
        )
        fb_img = st.file_uploader(
            label="スクリーンショットを追加していただくと、フィードバックを把握するうえで役立ちます",
            type=['jpg', 'jpeg', 'png'],
        )
        st.markdown('')
        col1, col2 = st.columns(2)
        with col1:
            st.button('クリア', on_click=clear_text_area, use_container_width=True)
        with col2:
            feedback_btn = st.button('送信', type='primary', icon=":material/send:", use_container_width=True)
        if feedback_btn:
            feedback(st.session_state.text_area_content, fb_img)


def c():
    st.markdown('C言語のページです。')


def python():
    st.title('Python入門編')
    container1 = st.container(border=True)
    with container1:
        st.markdown(
            '''
            **目次**
             1. [Pythonってどんな言語](#Pythonってどんな言語)
             2. [環境構築](#環境構築)
             3. [変数・データ型](#変数・データ型)
             4. [演算](#演算)
             5. [入出力処理](#入出力処理)
             6. [コメント](#コメント)
             7. [文字列処理](#文字列処理)
             8. [条件分岐](#条件分岐)
             9. [反復処理](#反復処理)
            10. [関数](#関数)
            11. [オブジェクト指向](#オブジェクト指向)
            12. [モジュール・パッケージ・ライブラリ](#モジュール・パッケージ・ライブラリ)
            13. [例外処理](#例外処理)
            14. [日付・時刻](#日付・時刻)
            15. [ファイル・ディレクトリ操作](#ファイル・ディレクトリ操作)
            16. [まとめ](#まとめ)
            17. [あとがき](#あとがき)
            '''
        )
    container2 = st.sidebar.container(border=True)
    with container2:
        st.markdown(
            '''
            **目次**
             1. [Pythonってどんな言語](#Pythonってどんな言語)
             2. [環境構築](#環境構築)
             3. [変数・データ型](#変数・データ型)
             4. [演算](#演算)
             5. [入出力処理](#入出力処理)
             6. [コメント](#コメント)
             7. [文字列処理](#文字列処理)
             8. [条件分岐](#条件分岐)
             9. [反復処理](#反復処理)
            10. [関数](#関数)
            11. [オブジェクト指向](#オブジェクト指向)
            12. [モジュール・パッケージ・ライブラリ](#モジュール・パッケージ・ライブラリ)
            13. [例外処理](#例外処理)
            14. [日付・時刻](#日付・時刻)
            15. [ファイル・ディレクトリ操作](#ファイル・ディレクトリ操作)
            16. [まとめ](#まとめ)
            17. [あとがき](#あとがき)
            '''
        )
    st.divider()

    st.header('1. Pythonってどんな言語', anchor='Pythonってどんな言語', divider='blue')
    st.markdown(
        '''
        Pythonは1991年にリリースされた人気のプログラミング言語です。\n
        最大の特長は、文法がシンプルでわかりやすい点。覚えやすいため初心者にも人気があります。\n
        一方、Pythonはインタプリタ型言語というソースコードを1行ずつ機械語に変換しながら実行する方式なので、
        C言語などのコンパイラ型言語に比べると処理速度が遅いなどの短所も存在します。\n
        ---
        Pythonは汎用性の高い言語なので、幅広い分野で開発に用いられています。\n
        最も使われているであろう分野は、人工知能分野です。そのほかにもweb開発関連で使われることがあります。\n
        '''
    )

    st.header('2. 環境構築', anchor='環境構築', divider='blue')
    st.markdown(
        '''
        Pythonがどんな言語なのかわかったら、環境構築をしましょう。\n
        Pythonの環境構築は大まかに以下の2つです。
        '''
    )
    st.subheader('2.1 Python本体', divider='green')
    st.markdown(
        '''
        Python本体とは、Pythonで書かれたプログラムを解釈し、実行するために必要なツールを指します。Pythonを動かすためには最低限必須です。\n
        [Pythonのインストール](https://www.python.org/downloads/)
        '''
    )
    st.subheader('2.2 開発環境', divider='green')
    st.markdown(
        '''
        Pythonプログラミングを効率化したい方は、開発環境もインストールしましょう。具体的には、「テキストエディタ」「統合開発環境（IDE）」の2種類を指します。

        テキストエディタは、Pythonのプログラムを効率的に書きやすくするためのソフトウェアです。統合開発環境は、プログラムの作成だけでなく実行やファイル管理など、開発に必要な機能をまとめて提供してくれます。

        [おすすめIDEその1：PyCharm](https://python-engineer.co.jp/pycharm-install/)\n
        [おすすめIDEその2：Visual Studio Code](https://qiita.com/mmake/items/55401c6a9e2f3f0f3475)
        '''
    )

    st.header('3. 変数・データ型', anchor='変数・データ型', divider='blue')
    st.markdown(
        '''
        プログラミングをする環境が整ったら、Pythonの文法について学んでいきましょう。\n
        まずは**変数**と**データ型**について学習しましょう。
        '''
    )
    st.subheader('3.1 変数とは', divider='green')
    st.markdown(
        '変数とは、数字や文字列などのデータを格納しておく「容器」のようなものです。Pythonに限らずプログラミングでは必ず使われるので、しっかり理解しましょう。')
    st.subheader('3.2 データ型とは', divider='green')
    st.markdown(
        '''
        データ型とは、各変数に「どのような種類のデータを入れられるか」という特質を規定するものです。\n
        Pythonは「動的型付け言語」で、実行時に変数へ入れるデータの種類によりデータ型が決まります。
        '''
    )
    img_path = os.path.join(os.path.dirname(__file__), '../img/type_list.png')
    st.image(os.path.normpath(img_path))

    st.subheader('4. 演算', anchor='演算', divider='blue')

    st.subheader('5. 入出力処理', anchor='入出力処理', divider='blue')

    st.subheader('6. コメント', anchor='コメント', divider='blue')

    st.subheader('7. 文字列処理', anchor='文字列処理', divider='blue')

    st.subheader('8. 条件分岐', anchor='条件分岐', divider='blue')

    st.subheader('9. 反復処理', anchor='反復処理', divider='blue')

    st.subheader('10. 関数', anchor='関数', divider='blue')

    st.subheader('11. オブジェクト指向', anchor='オブジェクト指向', divider='blue')

    st.subheader('12. モジュール・パッケージ・ライブラリ', anchor='モジュール・パッケージ・ライブラリ', divider='blue')

    st.subheader('13. 例外処理', anchor='例外処理', divider='blue')

    st.subheader('14. 日付・時刻', anchor='日付・時刻', divider='blue')

    st.subheader('15. ファイル・ディレクトリ操作', anchor='ファイル・ディレクトリ操作', divider='blue')

    st.subheader('16. まとめ', anchor='まとめ', divider='blue')

    st.subheader('17. あとがき', anchor='あとがき', divider='blue')