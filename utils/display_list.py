import streamlit as st
import mysql.connector

# 주유소 목록을 체크박스 조건에 따라 시각화
def display_oil(condition='all'):
    # 전체 주유소 목록 시각화
    if condition == 'all':
        for i in range(100): # 표시해야하는 주유소 목록만큼 반복
            with st.container():
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
                    if True: # 내 주유소 테이블에 없으면 빈별 이모지
                        my_oil_button = st.button('☆', key=i) # 각 주유소명을 키값으로 사용
                    else: # 내 주유소 테이블에 있으면 별 이모지
                        my_oil_button = st.button('⭐', key=i)

                st.divider()

    # 내 주유소 목록 시각화
    elif condition == 'my_oil':

    # 착한 주유소 목록 시각화
    elif condition == 'good_oil':

    # 내 주유소 and 착한 주유소 목록 시각화
    elif condition == 'my_good_oil':

# 주차장 목록을 체크박스 조건에 따라 시각화
def display_park(condition='all'):
    # 전체 주차장 목록 시각화
    if condition == 'all':
        for i in range(100): # 전체 주차장 목록만큼 반복
            with st.container():
                icon_col, park_info_col, my_park_button_col = st.columns([1, 4, 1])

                # 주차장 아이콘 레이아웃
                with icon_col:
                    st.subheader('🅿️')

                # 주차장 정보 레이아웃
                with park_info_col:
                    st.subheader('주차장명')
                    st.text('XX시 XX구 XX로')
                    st.text('00-0000-0000')

                # 찜버튼 레이아웃
                with my_park_button_col:
                    if True: # 내 주차장 테이블에 없으면 빈별 이모지
                        my_park_button = st.button('☆', key=i) # 각 주차장명을 키값으로 사용
                    else: # 내 주차장 테이블에 있으면 별 이모지
                        my_park_button = st.button('⭐, key=i') 

                st.divider()

    # 내 주차장 목록 시각화
    elif condition == 'my_park':


    
