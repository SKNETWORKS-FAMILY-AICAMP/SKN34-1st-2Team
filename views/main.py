import base64
import streamlit as st

st.set_page_config(layout="centered")

st.markdown("""
        <style>
        .st-link {
            display: flex;
            flex-flow: column;
            align-items: center;
            justify-content: center;
            height: calc(100vh - 60px - 18rem);
            text-decoration: none !important;
            color: #31333f !important;
            font-weight: 700;
        }

        @-webkit-keyframes fade-in {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
            }
            @keyframes fade-in {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
        
        .fade-in {
            -webkit-animation: fade-in 1.2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
            animation: fade-in 1.2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
        }
        </style>
""", unsafe_allow_html=True)

#이미지를 HTML에 바로 심을 수 있게 기기용 데이터로 바꾸는 함수
def get_image_link_html(file_path, link_target, width=200):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    src = f"data:image/png;base64,{b64}"

    # 하나의 덩어리로 HTML 구성
    return f'<a href="{link_target}" target="_self" class="st-link fade-in"><img src="{src}" style="width:{width}px;">당 신 의 주 유 / 주 차 를 빠 르 게 😋</a>'

logo_html = get_image_link_html("../assets/logo.png", "oil", width=400)
st.markdown(logo_html, unsafe_allow_html=True)