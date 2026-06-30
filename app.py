import streamlit as st

main = st.Page("views/main.py", title="메인")
parking = st.Page("views/parking.py", title="주차장")
oil = st.Page("views/oil.py", title="주유소")
faq = st.Page("views/faq.py", title="FAQ")
test = st.Page("views/test.py", title="테스트")

current_page = st.navigation([main, parking, oil, faq, test], position="hidden")

if current_page == main:
    pg = st.navigation([main, parking, oil, faq, test], position="hidden")
else:
    pg = st.navigation(
        {
            "": [main, parking, oil, faq, test]
        },
        position="top"  
    )

pg.run()

