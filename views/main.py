import streamlit as st
import components.sample as sp1
from services.api import api
import streamlit.components.v1 as components


#예시 재사용 컴포넌트
sp1.header() 
st.set_page_config(layout="wide")
    
parking_val = st.button('주차장')
gas_val = st.button('주유소')

kind = "parking"
kind_txt = "주차장"


if parking_val:
    kind = "parking"
    kind_txt = "주차장"
elif gas_val:
    kind = "gas"
    kind_txt = "주유소"

#주차장 주소로 검색 예시
search_val = st.text_input(f"{kind_txt} 주소 입력")
if search_val:
    pk_info = api.search_address(kind, search_val)
    st.write(pk_info)
else:
    st.write("주소입력")