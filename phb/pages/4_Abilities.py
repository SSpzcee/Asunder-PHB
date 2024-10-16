import streamlit as st

st.set_page_config(page_title="Abilities", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Abilities</h1>", unsafe_allow_html=True)

st.markdown("<a href='#chakra-abilities'>Chakra Abilities</a>", unsafe_allow_html=True)
st.markdown("<a href='#advanced-training'>Advanced Training</a>", unsafe_allow_html=True)
st.markdown("<a href='#genjutsu'>Genjutsu</a>", unsafe_allow_html=True)
st.markdown("<a href='#physical'>Physical</a>", unsafe_allow_html=True)
st.markdown("<a href='#sensory'>Sensory</a>", unsafe_allow_html=True)
st.markdown("<a href='#subtlety'>Subtlety</a>", unsafe_allow_html=True)
st.markdown("<a href='#equipment'>Equipment</a>", unsafe_allow_html=True)
st.markdown("<a href='#other'>Other</a>", unsafe_allow_html=True)
st.markdown("<a href='#skill'>Skill</a>", unsafe_allow_html=True)
st.markdown("<a href='#development'>Development</a>", unsafe_allow_html=True)

abilities = open("phb/md/Abilities.md", "r")
st.write(abilities.read())