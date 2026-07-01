import streamlit as st

main = st.Page("views/main.py", title="메인")
oil = st.Page("views/oil.py", title="주유소")
parking = st.Page("views/parking.py", title="주차장")
faq = st.Page("views/faq.py", title="FAQ")

current_page = st.navigation([main, parking, oil, faq], position="hidden")

if current_page == main:
    pg = st.navigation([main, oil, parking, faq], position="hidden")
else:
    pg = st.navigation(
        {
            "": [main, oil, parking, faq]
        },
        position="top"  
    )

pg.run()

