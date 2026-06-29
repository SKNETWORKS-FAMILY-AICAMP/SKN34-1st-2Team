import streamlit as st
from streamlit_extras.specialized_inputs import search_input

# 페이지 레이아웃을 꽉찬 화면으로 설정
st.set_page_config(layout='wide')

# 지도 레이아웃과 주유소 목록 레이아웃 나누기
map_col, list_col = st.columns([3, 2])

with map_col:
    # 지도 레이아웃 작성
    pass

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
    if search_q:
        # 검색 로직 구현
        pass

    # 주유소 목록 시각화
    for i in range(100): # 표시해야하는 주유소 목록만큼 반복
        with st.container():
            st.html('''
                <style>
                    .st-key-my_custom_container {
                        background-color: #e6f2ff;
                        padding: 20px;
                        border-radius: 10px;
                    }
                </style>        
            ''')
            icon_col, oil_info_col, my_oil_button_col = st.columns([1, 4, 1])
            # 주유소 아이콘 레이아웃
            with icon_col:
                st.subheader('⛽')
            # 주유소 정보 레이아웃
            with oil_info_col:
                st.subheader('주유소명')
                st.text('XX시 XX구 XX로')
                st.text('00-0000-0000')
            # 찜버튼 레이아웃
            with my_oil_button_col:
                my_oil_button = st.button('☆', key=i) # 각 주유소 이름을 키값으로 사용
            
            st.divider()