import streamlit as st

main = st.Page("views/main.py", title="메인")
oil = st.Page("views/oil.py", title="주유소")
parking = st.Page("views/parking.py", title="주차장")

pg = st.navigation(
    {
        "": [main, oil, parking]
    },
    position="top"  
)

pg.run()
    