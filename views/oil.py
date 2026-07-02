import streamlit as st
from streamlit_extras.specialized_inputs import search_input
import streamlit.components.v1 as components
import mysql.connector
from components.display_list import display_oil
import config as cf
from utils import kakao

# 페이지 레이아웃을 꽉찬 화면으로 설정
st.set_page_config(layout='wide')

# 주소값
if "oil_location" not in st.session_state:
    st.session_state.oil_location = "가산디지털1로 25 18층 플레이데이터" # 플레이데이터 주소

# st.session_state.oil_location: 검색한 주소값 
lat, lot = kakao.address_to_latlng(st.session_state.oil_location)

# 페이징 위한 세션 설정
if "oil_keyword" not in st.session_state:
    st.session_state.oil_keyword = ""

if "oil_page" not in st.session_state:
    st.session_state.oil_page = 1

# 지도 레이아웃과 주유소 목록 레이아웃 나누기
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
    <div id="map" style="width:100%;height:750px;"></div>

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
    components.html(html, height=750)
    
with list_col:
        # 주유소 목록 레이아웃 작성
        # 검색, 착한주유소 보기, 내 주유소 보기 라디오 버튼 생성
        oil_radio = st.radio(label='oil_radio', options = ['검색', '착한주유소 보기', '내 주유소 보기'], horizontal=True, label_visibility='hidden')

        # 검색창 생성
        search_q = search_input("Search", label_visibility="collapsed", key="ex_search")
        if search_q != "" and search_q != st.session_state.oil_keyword:
            # 검색 로직 구현
            st.session_state.oil_keyword = search_q
            st.session_state.oil_page = 1

        # 기본검색
        if st.session_state.oil_keyword:
            # 검색
            if oil_radio == '검색':
                mode = "all"
            # 착한주유소 보기
            elif oil_radio == '착한주유소 보기':
                mode = "my_oil"
            # 내 주유소 보기
            elif oil_radio == '내 주유소 보기':
                mode = "good_oil"

            display_oil(mode, st.session_state.oil_keyword)
            
        # 검색이 없을 때
        else:
            with st.container(height=650):
                st.markdown('<p style="text-align:center;padding:20px;">주소를 입력해 주세요.</p>', unsafe_allow_html=True)