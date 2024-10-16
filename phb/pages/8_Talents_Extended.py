import streamlit as st

st.set_page_config(page_title="Talents", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Talents</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 110px;
    }

</style>""", unsafe_allow_html=True)

gates, kage, nc, hyper = st.tabs(["Eight Gates", "Kage Bunshin", "Natural Chakra", "Hyper Elements"])

gatest = open("phb/md/Eight Gates.md", "r")
gates.write(gatest.read())

kaget = open("phb/md/Kage Bunshin.md", "r")
kage.write(kaget.read())

nct = open("phb/md/Natural Chakra.md", "r")
nc.write(nct.read())

hypert = open("phb/md/Hyper Elements.md", "r")
hyper.write(hypert.read())



