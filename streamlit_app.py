import streamlit as st

import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# ---- USER AUTHENTICATION ----------
names = ["Catarina Nunes", "Beatriz Monteiro", "Margarida Raposo", "Teresa Menezes"]
usernames = ["catarinagn", "bea_m", "magui", "teresa"]

file_path = Path("hashed_pw.pkl")
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(
    credentials={
        "usernames": {
            u: {"name": n, "password": p}
            for u, n, p in zip(usernames, names, hashed_passwords)
        }
    },
    cookie_name="FideBot", key="abcdef", cookie_expiry_days=30)

login_result = authenticator.login(location="main", fields={"form_name": "Login"})

if login_result:
    name, authentication_status, username = login_result

    if authentication_status is False:
        st.error("Username/Password is incorrect")
    elif authentication_status is None:
        st.warning("Please enter your username and password.")
    elif authentication_status:
        st.success(f"Welcome {name}!")

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
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}!")
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
else:
    st.warning("Submit your credentials, please.")
