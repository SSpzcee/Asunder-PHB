import streamlit as st

st.set_page_config(page_title="Abilities", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Abilities</h1>", unsafe_allow_html=True)



abilities = open("phb/md/Abilities.md", "r")
st.write(abilities.read())
