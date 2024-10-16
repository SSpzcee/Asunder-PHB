import streamlit as st

st.set_page_config(page_title="Summons", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Summoning Contracts</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 50px;
    }

</style>""", unsafe_allow_html=True)

details, avian, canine, feline, hare, monkey, salamander, slug, snake, spider, toad = st.tabs(["Details", "Avian", "Canine", "Feline", "Hare", "Monkey", "Salamander", "Slug", "Snake", "Spider", "Toad"])

detailst = open("phb/summon_md/details.md", "r")
details.write(detailst.read())

aviant = open("phb/summon_md/Avian.md", "r")
avian.write(aviant.read())

caninet = open("phb/summon_md/Canine.md", "r")
canine.write(caninet.read())

felinet = open("phb/summon_md/Feline.md", "r")
feline.write(felinet.read())

haret = open("phb/summon_md/Hare.md", "r")
hare.write(haret.read())

monkeyt = open("phb/summon_md/Monkey.md", "r")
monkey.write(monkeyt.read())

salamandert = open("phb/summon_md/Salamander.md", "r")
salamander.write(salamandert.read())

slugt = open("phb/summon_md/Slug.md", "r")
slug.write(slugt.read())

snaket = open("phb/summon_md/Snake.md", "r")
snake.write(snaket.read())

spidert = open("phb/summon_md/Spider.md", "r")
spider.write(spidert.read())

toadt = open("phb/summon_md/Toad.md", "r")
toad.write(toadt.read())
