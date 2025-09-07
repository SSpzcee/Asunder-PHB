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

rulese = open("phb/md/Equipment Rules.md", "r")
rules.write(rulese.read())

meleee = open("phb/md/Melee Weapons.md", "r")
melee.write(meleee.read())

rangede = open("phb/md/Ranged Weapons.md", "r")
ranged.write(rangede.read())

geare = open("phb/md/Gear.md", "r")
gear.write(geare.read())

tagse = open("phb/md/Exploding Tags.md", "r")
tags.write(tagse.read())

