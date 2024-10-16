import streamlit as st

st.set_page_config(page_title="Advancement", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Advancement</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 225px;
    }

</style>""", unsafe_allow_html=True)

adv, rb, tal = st.tabs(["Advancement", "Rank Benefits", "Talents"])

adva = open("phb/md/Advancement.md", "r")
adv.write(adva.read())

rb.markdown("<a href='#chuunin'>Chuunin</a>", unsafe_allow_html=True)
rb.markdown("<a href='#jounin'>Jounin</a>", unsafe_allow_html=True)
rb.markdown("<a href='#special-jounin'>Special Jounin</a>", unsafe_allow_html=True)
rb.markdown("<a href='#anbu'>ANBU</a>", unsafe_allow_html=True)

rba = open("phb/md/Rank Benefits.md", "r")
rb.write(rba.read())

tal.markdown("<a href='#acquiring-talents'>Acquiring Talents</a>", unsafe_allow_html=True)
tal.markdown("<a href='#enhancements'>Enhancements</a>", unsafe_allow_html=True)
tal.markdown("<a href='#capabilities'>Capabilities</a>", unsafe_allow_html=True)

tala = open("phb/md/Talents.md", "r")
tal.write(tala.read())