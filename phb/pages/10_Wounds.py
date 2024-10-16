import streamlit as st

st.set_page_config(page_title="Wounds", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Wounds</h1>", unsafe_allow_html=True)

st.markdown("<a href='#blunt'>Blunt</a>", unsafe_allow_html=True)
st.markdown("<a href='#slashing'>Slashing</a>", unsafe_allow_html=True)
st.markdown("<a href='#piercing'>Piercing</a>", unsafe_allow_html=True)
st.markdown("<a href='#energy'>Energy</a>", unsafe_allow_html=True)

wound = open("phb/md/Wounds.md", "r")
st.write(wound.read())
