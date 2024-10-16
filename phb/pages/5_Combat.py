import streamlit as st

st.set_page_config(page_title="Combat", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Combat</h1>", unsafe_allow_html=True)

st.markdown("<a href='#initiative'>Initiative</a>", unsafe_allow_html=True)
st.markdown("<a href='#actions'>Actions</a>", unsafe_allow_html=True)
st.markdown("<a href='#attacking'>Attacking</a>", unsafe_allow_html=True)
st.markdown("<a href='#stealth'>Stealth</a>", unsafe_allow_html=True)
st.markdown("<a href='#pursuit'>Pursuit</a>", unsafe_allow_html=True)
st.markdown("<a href='#conditions-and-status'>Conditions and Status</a>", unsafe_allow_html=True)
st.markdown("<a href='#weather-conditions'>Weather Conditions</a>", unsafe_allow_html=True)
st.markdown("<a href='#fatigue'>Fatigue</a>", unsafe_allow_html=True)
st.markdown("<a href='#recovery'>Recovery</a>", unsafe_allow_html=True)

combat = open("phb/md/Combat.md", "r")
st.write(combat.read())