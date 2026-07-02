import streamlit as st
from streamlit_extras.specialized_inputs import search_input
import streamlit.components.v1 as components
import mysql.connector
from components.display_list import display_park
import config as cf
from utils import kakao

# 페이지 레이아웃을 꽉찬 화면으로 설정
st.set_page_config(layout='wide')

# 주소값
if "park_location" not in st.session_state:
    st.session_state.park_location = "가산디지털1로 25 18층 플레이데이터" # 플레이데이터 주소

# st.session_state.park_location: 검색한 주소값 
lat, lot = kakao.address_to_latlng(st.session_state.park_location)

# 페이징 위한 세션 설정
if "park_keyword" not in st.session_state:
    st.session_state.park_keyword = ""

if "parking_page" not in st.session_state:
    st.session_state.parking_page = 1

# 지도 레이아웃과 주차장 목록 레이아웃 나누기
map_col, list_col = st.columns([3, 2])

with map_col:
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <script src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={cf.KAKAO_MAP_KEY}"></script>
    </head>

    <body style="margin:0;">
    <div id="map" style="width:100%;height:790px;"></div>

    <script>

    var mapContainer = document.getElementById('map');
    
    var mapOption = {{
        center: new kakao.maps.LatLng({lat}, {lot}),
        level: 3
    }};

    var map = new kakao.maps.Map(mapContainer, mapOption);

    var markerPosition = new kakao.maps.LatLng({lat}, {lot});

    var marker = new kakao.maps.Marker({{
        position: markerPosition
    }});

    marker.setMap(map);

    </script>

    </body>
    </html>
    """
    components.html(html, height=790)
    
with list_col:
    # 주차장 목록 레이아웃 작성
    # 검색, 내 주차장 보기 라디오 버튼 생성
    park_radio = st.radio(label='park_radio', options = ['검색', '내 주차장 보기'], horizontal=True, label_visibility='hidden')

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
        with st.container(height=650):
            st.markdown('<p style="text-align: center; padding: 20px 0;">검색된 내용이 없습니다.</p>', unsafe_allow_html=True)
