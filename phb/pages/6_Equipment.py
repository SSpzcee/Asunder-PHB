import streamlit as st

st.set_page_config(page_title="Equipment", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Equipment</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 50px;
    }

</style>""", unsafe_allow_html=True)

rules, melee, ranged, gear, tags, poison = st.tabs(["Weapon Rules", "Melee Weapons", "Ranged Weapons", "Gear", "Explosive Tags", "Poisons"])





