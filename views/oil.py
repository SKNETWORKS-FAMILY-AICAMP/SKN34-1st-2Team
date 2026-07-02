import streamlit as st
from streamlit_extras.specialized_inputs import search_input
import streamlit.components.v1 as components
import mysql.connector
from components.display_list import display_oil
import config as cf

# 페이지 레이아웃을 꽉찬 화면으로 설정
st.set_page_config(layout='wide')

# 위도, 경도 값
if "location" not in st.session_state:
    st.session_state.location = [37.4682, 126.8861] # 플레이데이터 위도, 경도

lat, lot = st.session_state.location

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
    <script src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={cf.KAKAO_MAP_KEY}&libraries=services"></script>
    </head>

    <body style="margin:0;">
    <div id="map" style="width:100%;height:750px;"></div>

    <script>

    var mapContainer = document.getElementById('map');

    var mapOption = {{
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
    }};

    var map = new kakao.maps.Map(mapContainer, mapOption);

    var geocoder = new kakao.maps.services.Geocoder();

    geocoder.addressSearch("제주특별자치도 제주시 첨단로 242", function(result, status) {{

        if (status === kakao.maps.services.Status.OK) {{

            var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

            // 마커 생성
            var marker = new kakao.maps.Marker({{
                position: coords
            }});

            // 지도에 마커 표시
            marker.setMap(map);

            // 인포윈도우
            var infowindow = new kakao.maps.InfoWindow({{
                content: '<div style="padding:5px;text-align:center;">지도</div>'
            }});

            infowindow.open(map, marker);

            // 지도 중심 이동
            map.setCenter(coords);
        }}
    }});
console.log(coords);
    </script>

    </body>
    </html>
    """

    components.html(html, height=750)
    
with list_col:
        # 주유소 목록 레이아웃 작성
        # 착한주유소 보기와 내 주유소 보기 체크박스 생성
        checkbox_good, checkbox_my = st.columns([1, 1])
        with checkbox_good:
            is_good_oil = st.checkbox('착한주유소 보기')
        with checkbox_my:
            is_my_oil = st.checkbox('내 주유소 보기')

        # 검색창 생성
        search_q = search_input("Search", label_visibility="collapsed", key="ex_search")
        if search_q != "" and search_q != st.session_state.oil_keyword:
            # 검색 로직 구현
            st.session_state.oil_keyword = search_q
            st.session_state.oil_page = 1

        # 검색을 하지 않으면 주차장 테이블 전체 표시
        if st.session_state.oil_keyword:
            display_oil("all", st.session_state.oil_keyword)
        else:
            with st.container(height=650):
                st.markdown('<p style="text-align:center;padding:20px;">주소를 입력해 주세요.</p>', unsafe_allow_html=True)