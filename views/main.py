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
        </style>
""", unsafe_allow_html=True)
# 1. 이미지를 HTML에 바로 심을 수 있게 기기용 데이터로 바꾸는 함수
def get_image_link_html(file_path, link_target, width=200):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    src = f"data:image/png;base64,{b64}"

    # 하나의 덩어리로 HTML 구성
    return f'<a href="{link_target}" target="_self" class="st-link"><img src="{src}" style="width:{width}px;">당 신 의 주 유 / 주 차 를 빠 르 게 😋</a>'

#주차장 주소로 검색 예시
search_val = st.text_input(f"{kind_txt} 주소 입력")
if search_val:
    pk_info = api.search_address(kind, search_val)
    st.write(pk_info)
else:
    st.write("주소입력")
