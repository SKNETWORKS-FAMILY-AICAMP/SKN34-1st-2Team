import streamlit as st
from services.api import api
from services.wish_control import is_wish, toggle_wish
import mysql.connector
import math

# 주유소 목록을 체크박스 조건에 따라 시각화
def display_oil(condition='all', keyword=""):  # all, my_oil, good_oil
    # 형식 통일
    if condition == 'all':
        data = api.search_address('oil', keyword)
        name = "conmNm"
        addr1 = "lctnRoadNm" # 도로명
        addr2 = "lctnLotnoAddr" #지번
        tel = "telno"
        lat = "lat"
        lot = "lot"
        tip = "rprsvNm"

    # 내 주유소 목록 시각화
    elif condition == 'my_oil':
        data = api.search_address('oil', keyword)
        name = "conmNm"
        addr = "lctnRoadNm"    
        tel = "telno"
        lat = "lat"
        lot = "lot"
        tip = "rprsvNm"

    # 착한 주유소 목록 시각화
    elif condition == 'good_oil':
        data = api.search_address('oil', keyword)
        name = "conmNm"
        addr = "lctnRoadNm"    
        tel = "telno"
        lat = "lat"
        lot = "lot"
        tip = "rprsvNm"

    # 주유소 명으로 불러오기
    # api_val = api.search_name('oil', '(주)대농석유 남태령주유소')
    # st.write(api_val[0][addr])

    # 페이징
    PAGE_SIZE = 3      # 한 페이지당 데이터 개수
    BLOCK_SIZE = 5     # 페이지 버튼 개수

    if "oil_page" not in st.session_state:
        st.session_state.oil_page = 1

    total_pages = max(1, math.ceil(len(data) / PAGE_SIZE))

    # 현재 페이지 보정
    st.session_state.oil_page = min(
        max(1, st.session_state.oil_page),
        total_pages
    )

    # 현재 페이지 데이터
    start = (st.session_state.oil_page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE
    page_items = data[start:end]

    # 전체 주유소 목록 시각화
    if condition == 'all':
        with st.container(height=650):
            for idx, i in enumerate(page_items):  # 현재 페이지에 표시해야 하는 주유소 목록만큼 반복
                icon_col, oil_info_col, my_oil_button_col = st.columns([1, 4, 1])

                # 주유소 아이콘 레이아웃
                with icon_col:
                    st.subheader('⛽')

                # 주유소 정보 레이아웃
                with oil_info_col:
                    # 유가 정보 db에서 받아와서 툴팁에 작성
                    st.subheader(i[name], help=i.get('tmp', ""))
                    st.text(i[addr1] if i[addr1] else i[addr2])
                    st.text(i[tel] if i[tel] else "번호없음")

                with my_oil_button_col:
                    if st.button("선택", key=i[name]):
                        st.session_state.oil_location = i[addr1] if i[addr1] else i[addr2]
                        st.rerun()
                        
                    # 찜버튼 레이아웃
                    if not is_wish('o', i[name], i[addr]):  # 내 주유소 테이블에 없으면 빈별 이모지
                        if st.button(
                            '☆',
                            key=f"oil_{i[name]}"
                        ):
                            toggle_wish('o', i[name], i[addr], i[tel], False) # 클릭하면 테이블에 추가
                            st.rerun()

                    else:  # 내 주유소 테이블에 있으면 별 이모지
                        if st.button(
                            '⭐',
                            key=f"oil_{i[name]}"
                        ):
                            toggle_wish('o', i[name], i[addr], i[tel], True) # 클릭하면 테이블에서 삭제
                            st.rerun()

                if idx + 1< len(page_items):
                    st.divider()
                else:
                    st.markdown('<div style="disply: block; height: 55px;"></div>', unsafe_allow_html=True)
                
            if not data:
                # 검색 내용이 없으면
                st.markdown('<p style="text-align:center;padding:20px;">검색된 내용이 없습니다.</p>', unsafe_allow_html=True)

    if data:
        # 페이지 버튼 UI
        current_block = (st.session_state.oil_page - 1) // BLOCK_SIZE

        start_page = current_block * BLOCK_SIZE + 1
        end_page = min(start_page + BLOCK_SIZE - 1, total_pages)

        cols = st.columns(BLOCK_SIZE + 2)

        # ◀ 이전 블록
        with cols[0]:
            if st.button("◀"):
                if start_page > 1:
                    st.session_state.oil_page = start_page - BLOCK_SIZE
                    st.rerun()

        # 페이지 번호
        for idx, page in enumerate(range(start_page, end_page + 1), start=1):
            with cols[idx]:
                if st.button(str(page), key=f"page_{page}"):
                    st.session_state.oil_page = page
                    st.rerun()

        # ▶ 다음 블록
        with cols[-1]:
            if st.button("▶"):
                if end_page < total_pages:
                    st.session_state.oil_page = end_page + 1
                    st.rerun()
                    
        # st.write(f"현재 페이지 : {st.session_state.oil_page}")
                
# 주차장 목록을 체크박스 조건에 따라 시각화
def display_park(condition='all', keyword=""): # all, my_park 중 택일
    if condition == 'all':
        data = api.search_address('park', keyword)
        name = "prkplceNm"
        addr = "rdnmadr"   
        addr1 = "rdnmadr" # 도로명
        addr2 = "lnmadr" #지번 
        tel = "phoneNumber"
    
    # 페이징
    PAGE_SIZE = 3      # 한 페이지당 데이터 개수
    BLOCK_SIZE = 5     # 페이지 버튼 개수

    if "park_page" not in st.session_state:
        st.session_state.park_page = 1

    total_pages = max(1, math.ceil(len(data) / PAGE_SIZE))

    # 현재 페이지 보정
    st.session_state.park_page = min(
        max(1, st.session_state.park_page),
        total_pages
    )

    # 현재 페이지 데이터
    start = (st.session_state.park_page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE
    page_items = data[start:end]

    # 전체 주차장 목록 시각화
    if condition == 'all':
        with st.container(height=650):
            for idx, i in enumerate(page_items):  # 현재 페이지에 표시해야 하는 주유소 목록만큼 반복
                with st.container():
                    icon_col, park_info_col, my_park_button_col = st.columns([1, 4, 1])

                    # 주차장 아이콘 레이아웃
                    with icon_col:
                        st.subheader('🅿️')

                    # 주차장 정보 레이아웃
                    with park_info_col:
                        st.subheader(i[name], help=i.get('tmp', ""))
                        st.text(i[addr1] if i[addr1] else i[addr2])
                        st.text(i[tel] if i[tel] else "번호없음")

                    # 찜버튼 레이아웃
                    with my_park_button_col:
                        if st.button("선택", key=i[name]):
                            st.session_state.park_location = i[addr1] if i[addr1] else i[addr2]
                            st.rerun()
                            
                        if not is_wish('p', i[name], i[addr]): # 내 주차장 테이블에 없으면 빈별 이모지
                            if st.button('☆', key=f"oil_{i[name]}"): 
                                toggle_wish('p', i[name], i[addr], i[tel], False)
                                st.rerun()
                        else: # 내 주차장 테이블에 있으면 별 이모지
                            if st.button('⭐', key=f"oil_{i[name]}"):
                                toggle_wish('p', i[name], i[addr], i[tel], True) 
                                st.rerun()

                    if idx + 1< len(page_items):
                        st.divider()
                    else:
                        st.markdown('<div style="disply: block; height: 55px;"></div>', unsafe_allow_html=True)
                    if not data:
                        # 검색 내용이 없으면
                        st.markdown('<p style="text-align:center;padding:20px;">검색된 내용이 없습니다.</p>', unsafe_allow_html=True)
                
    # 내 주차장 목록 시각화
    elif condition == 'my_park':
        pass
    
    if data:
        # 페이지 버튼 UI
        current_block = (st.session_state.park_page - 1) // BLOCK_SIZE

        start_page = current_block * BLOCK_SIZE + 1
        end_page = min(start_page + BLOCK_SIZE - 1, total_pages)

        cols = st.columns(BLOCK_SIZE + 2)

        # ◀ 이전 블록
        with cols[0]:
            if st.button("◀"):
                if start_page > 1:
                    st.session_state.park_page = start_page - BLOCK_SIZE
                    st.rerun()

        # 페이지 번호
        for idx, page in enumerate(range(start_page, end_page + 1), start=1):
            with cols[idx]:
                if st.button(str(page), key=f"page_{page}"):
                    st.session_state.park_page = page
                    st.rerun()

        # ▶ 다음 블록
        with cols[-1]:
            if st.button("▶"):
                if end_page < total_pages:
                    st.session_state.park_page = end_page + 1
                    st.rerun()
                    
        # st.write(f"현재 페이지 : {st.session_state.park_page}")


    
