import streamlit as st

st.set_page_config(page_title="Abilities", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Abilities</h1>", unsafe_allow_html=True)

st.markdown("<a href='#Physical'>Physical</a>", unsafe_allow_html=True)
st.markdown("<a href='#Chakra'>Chakra</a>", unsafe_allow_html=True)
st.markdown("<a href='#Genjutsu'>Genjutsu</a>", unsafe_allow_html=True)
st.markdown("<a href='#Sensory'>Sensory</a>", unsafe_allow_html=True)
st.markdown("<a href='#Subtlety'>Subtlety</a>", unsafe_allow_html=True)
st.markdown("<a href='#Supplementary'>Supplementary</a>", unsafe_allow_html=True)
st.markdown("<a href='#Equipment'>Equipment</a>", unsafe_allow_html=True)
st.markdown("<a href='#Advanced-Training'>Advanced Training</a>", unsafe_allow_html=True)
st.markdown("<a href='#Skill'>Skill</a>", unsafe_allow_html=True)
st.markdown("<a href='#Development'>Development</a>", unsafe_allow_html=True)

abilities = open("phb/md/Abilities.md", "r")
st.write(abilities.read())
