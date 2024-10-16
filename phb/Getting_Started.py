import streamlit as st

st.set_page_config(page_title="NW Asunder", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Welcome to Naruto World Asunder!</h1>", unsafe_allow_html=True)

st.image("phb/background.jpg", caption=None, use_column_width="always")

st.markdown("<a href='https://discord.gg/WUdQZAWsSr'>Join our discord!</a>", unsafe_allow_html=True)

gs = open("phb/md/Getting Started.md", "r")
st.write(gs.read())