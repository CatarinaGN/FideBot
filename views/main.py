import streamlit as st

st.title("Home Page")

# Center the logo
st.image("assets/logo.png", use_container_width=True)

# Explanation text below the logo
st.write("""
This interface is designed for the **ABCDEats Marketing Team** to visualize the company's clusters data, 
make predictions about a certain record, and write their own suggestions as well. 
It provides an easy-to-use interface for interacting with the clustering and prediction models.
""")