import streamlit as st

st.set_page_config(page_title="Villages", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Villages</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 75px;
    }

</style>""", unsafe_allow_html=True)

konoha, kumo, suna, iwa, kiri = st.tabs(["Konohagakure", "Kumogakure", "Sunagakure", "Iwagakure", "Kirigakure"])

konoha.header("Konohagakure")
konoha.write("flavor text here")
konoha.markdown("----")

konoha.markdown("<a href='#aburame'>Aburame</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#akimichi'>Akimichi</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#inuzuka'>Inuzuka</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#hyuuga'>Hyuuga</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#nara'>Nara</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#senju'>Senju</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#uchiha'>Uchiha</a>", unsafe_allow_html=True)
konoha.markdown("<a href='#asashi'>Asashi</a>", unsafe_allow_html=True)

konomd = open("phb/md/Konoha Clans.md", "r")
konoha.write(konomd.read())

kumo.header("Kumogakure")
kumo.write("flavor text here")
kumo.markdown("----")

kumo.markdown("<a href='#ba940a52'>Fūryosu</a>", unsafe_allow_html=True)
kumo.markdown("<a href='#chinoike'>Chinoike</a>", unsafe_allow_html=True)
kumo.markdown("<a href='#267e441f'>Saishihō</a>", unsafe_allow_html=True)
kumo.markdown("<a href='#kanato'>Kanato</a>", unsafe_allow_html=True)
kumo.markdown("<a href='#yurigami'>Yurigami</a>", unsafe_allow_html=True)
kumo.markdown("<a href='#taro'>TARO</a>", unsafe_allow_html=True)

kumomd = open("phb/md/Kumo Clans.md", "r")
kumo.write(kumomd.read())

suna.header("Sunagakure")
suna.write("flavor text here")
suna.markdown("----")

suna.markdown("<a href='#henzaki'>Henzaki</a>", unsafe_allow_html=True)
suna.markdown("<a href='#hitori'>Hitori</a>", unsafe_allow_html=True)
suna.markdown("<a href='#juugo-sato'>Juugo Sato</a>", unsafe_allow_html=True)
suna.markdown("<a href='#kairaishi'>Kairaishi</a>", unsafe_allow_html=True)
suna.markdown("<a href='#monkasei'>Monkasei</a>", unsafe_allow_html=True)
suna.markdown("<a href='#sabechi'>Sabechi</a>", unsafe_allow_html=True)
suna.markdown("<a href='#hakubai'>Hakubai</a>", unsafe_allow_html=True)

sunamd = open("phb/md/Suna Clans.md", "r")
suna.write(sunamd.read())

iwa.header("Iwagakure")
iwa.write("""Nestled deep within towering cliffs and surrounded by jagged mountains, Iwagakure no Sato is a testament to resilience and unyielding will. The village is built into a mountain itself, with homes, training grounds, and halls crafted and shaped seamlessly into the mountainside, blending the natural stone with theTsuchi Vanguard’s ingenuity. Mist often cloaks the streets in the early hours, giving it an air of mystery, while the ever-present sound of stone grinding underfoot reflects the hard lives of its people. The rigid, defensive layout of the village mirrors the Iwagakure way—adapt to the earth’s strength, endure every hardship, and never allow weakness to take root. The people of Iwa are as unshakeable as the stones they live among, valuing loyalty, hard work, and the security of their land above all else.
\n\nAs a military powerhouse well known for their resources, Iwagakure's shinobi excel in Earth Release techniques and the art of the Trade, leveraging their natural surroundings for both offense and defense. Many of its ninja hold a pragmatic worldview, understanding the sacrifices needed to maintain power in a turbulent world. Trust is earned slowly and broken rarely, making bonds within the village tight but guarded against outsiders. Under the guidance of the Tsuchikage, the village balances tradition and innovation, with veterans mentoring the next generation to safeguard Iwa’s legacy. Every crack in a stone tells a story, and in Iwagakure, even the smallest fragment of rock is a reminder that strength lies not in perfection, but in the ability to withstand.
""")
iwa.markdown("----")

iwa.markdown("<a href='#kidosei'>Kidosei</a>", unsafe_allow_html=True)
iwa.markdown("<a href='#tekketsu'>Tekketsu</a>", unsafe_allow_html=True)
iwa.markdown("<a href='#soma'>Soma</a>", unsafe_allow_html=True)
iwa.markdown("<a href='#yogani'>Yogani</a>", unsafe_allow_html=True)
iwa.markdown("<a href='#tesso'>Tesso</a>", unsafe_allow_html=True)

iwamd = open("phb/md/Iwa Clans.md", "r")
iwa.write(iwamd.read())

kiri.header("Kirigakure")
kiri.write("flavor text here")
kiri.markdown("----")

kiri.markdown("<a href='#sword-corps'>Sword Corps</a>", unsafe_allow_html=True)
kiri.markdown("<a href='#terumi'>Terumi</a>", unsafe_allow_html=True)
kiri.markdown("<a href='#touu'>Touu</a>", unsafe_allow_html=True)
kiri.markdown("<a href='#hozuki'>Hozuki</a>", unsafe_allow_html=True)
kiri.markdown("<a href='#niou'>Niou</a>", unsafe_allow_html=True)
kiri.markdown("<a href='#kaguya'>Kaguya</a>", unsafe_allow_html=True)
kiri.markdown("<a href='#watanabe'>Watanabe</a>", unsafe_allow_html=True)

kirimd = open("phb/md/Kiri Clans.md", "r")
kiri.write(kirimd.read())
