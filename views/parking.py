import streamlit as st
from streamlit_extras.specialized_inputs import search_input
import mysql.connector
from utils.display_list import display_park

# 페이지 레이아웃을 꽉찬 화면으로 설정
st.set_page_config(layout='wide')

# 지도 레이아웃과 주차장 목록 레이아웃 나누기
map_col, list_col = st.columns([3, 2])

with map_col:
    # 지도 레이아웃 작성
    pass

with list_col:
    # 주차장 목록 레이아웃 작성
    # 내 주차장 보기 체크박스 생성
    is_my_oil = st.checkbox('내 주차장 보기')

    # 검색창 생성
    search_q = search_input("Search", label_visibility="collapsed", key="ex_search")
    if search_q:
        # 검색 로직 구현
        pass

    # 검색을 하지 않으면 주차장 테이블 전체 표시
    else:
        display_park('all')
