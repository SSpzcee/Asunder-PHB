import streamlit as st

st.set_page_config(page_title="Jutsu", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Jutsu</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 150px;
    }

</style>""", unsafe_allow_html=True)

rules, nin, tai, gen = st.tabs(["Jutsu Rules", "Ninjutsu", "Taijutsu", "Genjutsu"])

rules.markdown("<a href='taijutsu'>Taijutsu</a>", unsafe_allow_html=True)
rules.markdown("<a href='ninjutsu'>Ninjutsu</a>", unsafe_allow_html=True)
rules.markdown("<a href='genjutsu'>Genjutsu</a>", unsafe_allow_html=True)

rulesj = open("phb/md/Jutsu.md", "r")
rules.write(rulesj.read())

nin.markdown("<a href='#general'>General</a>", unsafe_allow_html=True)
nin.markdown("<a href='#doton'>Doton</a>", unsafe_allow_html=True)
nin.markdown("<a href='#fuuton'>Fuuton</a>", unsafe_allow_html=True)
nin.markdown("<a href='#katon'>Katon</a>", unsafe_allow_html=True)
nin.markdown("<a href='#raiton'>Raiton</a>", unsafe_allow_html=True)
nin.markdown("<a href='#suiton'>Suiton</a>", unsafe_allow_html=True)
nin.markdown("<a href='#medical'>Medical</a>", unsafe_allow_html=True)
nin.markdown("<a href='#sealing'>Sealing</a>", unsafe_allow_html=True)

ninj = open("phb/md/Ninjutsu.md", "r")
nin.write(ninj.read())

tai.markdown("<a href='#unarmed'>Unarmed</a>", unsafe_allow_html=True)
tai.markdown("<a href='#combo'>Combo</a>", unsafe_allow_html=True)
tai.markdown("<a href='#weapon'>Weapon</a>", unsafe_allow_html=True)
tai.markdown("<a href='#grapple'>Grapple</a>", unsafe_allow_html=True)

taij = open("phb/md/Taijutsu.md", "r")
tai.write(taij.read())

gen.markdown("<a href='#e-rank'>E-Rank</a>", unsafe_allow_html=True)
gen.markdown("<a href='#d-rank'>D-Rank</a>", unsafe_allow_html=True)
gen.markdown("<a href='#c-rank'>C-Rank</a>", unsafe_allow_html=True)
gen.markdown("<a href='#b-rank'>B-Rank</a>", unsafe_allow_html=True)
gen.markdown("<a href='#a-rank'>A-Rank</a>", unsafe_allow_html=True)

genj = open("phb/md/Genjutsu.md", "r")
gen.write(genj.read())
