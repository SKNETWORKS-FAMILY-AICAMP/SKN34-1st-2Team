import streamlit as st
import components.sample as sp1
from services.db import db
from services.api import api

st.set_page_config(page_title="앱")

#예시 재사용 컴포넌트
sp1.header()

#예시 db 및 api 정보 불러오기
st.write(db.connect())
st.write(api.connect())

main = st.Page("pages/main.py", title="메인")
sample1 = st.Page("pages/sample1.py", title="샘플1")

pg = st.navigation([main, sample1])
pg.run()