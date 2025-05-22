import streamlit as st

#import streamlit_authenticator as stauth

# ---- PAGES SETUP -----
main_page = st.Page(
    page="views/main.py",
    title="Home Page",
    icon="🏠",
    default=True
)

fidebot_page = st.Page(
    page="views/cluster_prediction.py",
    title="FideBot",
    icon="🤖",
)

note_page = st.Page(
    page="views/cluster_analysis.py",
    title="As tuas Notas",
    icon="📋",
)

suggestions_page = st.Page(
    page="views/suggestions.py",
    title="Sugestões",
    icon="📩",
)

# --- Navigation Setup ----

pg = st.navigation(
    {
        "Home": [main_page],
        "Para ti": [fidebot_page, note_page, suggestions_page],
    }
)
#-- on all pages ----
st.logo(r"assets\logo.png", size="large")
st.sidebar.text("Made by Group P for Business Cases with Data Science 24/25 NOVA IMS")

pg.run()