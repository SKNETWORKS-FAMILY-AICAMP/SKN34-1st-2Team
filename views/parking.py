import streamlit as st
from streamlit_extras.specialized_inputs import search_input
import mysql.connector
from components.display_list import display_park

# 페이지 레이아웃을 꽉찬 화면으로 설정
st.set_page_config(layout='wide')

# 지도 레이아웃과 주차장 목록 레이아웃 나누기
map_col, list_col = st.columns([3, 2])

with map_col:
    # 지도 레이아웃 작성
    pass

with list_col:
    # 주차장 목록 레이아웃 작성
    # 검색, 내 주차장 보기 라디오 버튼 생성
    park_radio = st.radio(label='park_radio', options = ['검색', '내 주차장 보기'], horizontal=True)

    # 검색창 생성
    search_q = search_input("Search", label_visibility="collapsed", key="ex_search")
    if search_q:
        # 검색 로직 구현
        display_park('all', search_q)
    # 내 주차장 보기
    elif park_radio == '내 주차장 보기':
        display_park('my_park')
    # 검색이 없을 때
    else:
        st.markdown('<p style="text-align: center; padding: 20px 0;">검색된 내용이 없습니다.</p>', unsafe_allow_html=True)
