import streamlit as st

st.set_page_config(page_title="Uniques", page_icon="phb/logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("<h1 style='text-align: center;'>Uniques</h1>", unsafe_allow_html=True)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 85px;
    }

</style>""", unsafe_allow_html=True)

st.write("""
	Uniques are one of the many ways in which you can customize your character, giving you effects and capabilities that typically cannot be acquired otherwise. You gain five Unique Points to spend at character creation. Uniques are grouped by cost, with Creation Uniques all costing 1 point each. You can only have a maximum of 2 Creation Uniques.

However, you may save your unique points for later, if you want. As your character reaches certain EXP thresholds, they'll gain more unique points. You can either save these for later, spend them to acquire new uniques, or use them to upgrade existing ones. Regardless, you may only take a single unique once; you cannot, for example, take Endless Energy twice to get double its bonuses.

Some uniques have, below their descriptions, entries such as "Upgrades Into" and "Upgrades From." To upgrade a unique, you need to pay the difference between the cost of your current unique and the cost of the unique you will be upgrading it to. When you do this, you remove the old unique and replace it with the new one. This does mean that you might lose some effects entirely in the process.

You can ultimately have a maximum of 10 (11 if you’re Clanless) Unique Points, 5 at Creation and 5 from XP for a normal character. These uniques are unlocked at the following XP thresholds:

\n\n2000
\n3000
\n4500
\n6000
\n7000
""")

cup, oneup, twoup, threeup = st.tabs(["Creation Uniques", "1 Point Uniques", "2 Point Uniques", "3 Point Uniques"])

cup.markdown("<a href='#analyst'>Analyst</a>", unsafe_allow_html=True)
cup.markdown("<a href='#berserker'>Berserker</a>", unsafe_allow_html=True)
cup.markdown("<a href='#competitive'>Competitive</a>", unsafe_allow_html=True)
cup.markdown("<a href='#defender'>Defender</a>", unsafe_allow_html=True)
cup.markdown("<a href='#energetic'>Energetic</a>", unsafe_allow_html=True)
cup.markdown("<a href='#genius'>Genius</a>", unsafe_allow_html=True)
cup.markdown("<a href='#juggernaut'>Juggernaut</a>", unsafe_allow_html=True)
cup.markdown("<a href='#killer'>Killer</a>", unsafe_allow_html=True)
cup.markdown("<a href='#large'>Large</a>", unsafe_allow_html=True)
cup.markdown("<a href='#lucky'>Lucky</a>", unsafe_allow_html=True)
cup.markdown("<a href='#naturalist'>Naturalist</a>", unsafe_allow_html=True)
cup.markdown("<a href='#nimble'>Nimble</a>", unsafe_allow_html=True)
cup.markdown("<a href='#small'>Small</a>", unsafe_allow_html=True)
cup.markdown("<a href='#skilled-shinobi'>Skilled Shinobi</a>", unsafe_allow_html=True)
cup.markdown("<a href='#specialist'>Specialist</a>", unsafe_allow_html=True)
cup.markdown("<a href='#warder'>Warder</a>", unsafe_allow_html=True)

cupmd = open("phb/md/cup.md", "r")
cup.write(cupmd.read())

oneup.markdown("<a href='#alet'>Alert</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#applied-knowledge'>Applied Knowledge</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#blur'>Blur</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#close-ties'>Close Ties</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#chemist'>Chemist</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#elementally-gifted'>Elementally Gifted</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#expansive-chakra'>Expansive Chakra</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#entrepreneur'>Entrepreneur</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#hidden-potential'>Hidden Potential</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#indefatigable'>Indefatigable</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#killing-intent'>Killing Intent</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#lightfoot'>Lightfoot</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#martial-prowess'>Martial Prowess</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#nimble-hands'>Nimble Hands</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#silver-tongued'>Silver Tongued</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#scheduled'>Scheduled</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#seal-master'>Seal Master</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#weapon-master'>Weapon Master</a>", unsafe_allow_html=True)
oneup.markdown("<a href='#weight-trainer'>Weight Trainer</a>", unsafe_allow_html=True)

oneupmd = open("phb/md/oneup.md", "r")
oneup.write(oneupmd.read())

twoup.markdown("<a href='#boundless-chakra'>Boundless Chakra</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#bruiser'>Bruiser</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#chakra-sensor'>Chakra Sensor</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#cunning'>Cunning</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#determined'>Determined</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#elemental-mastery'>Elemental Mastery</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#endless-energy'>Endless Energy</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#exceptionally-fast'>Exceptionally Fast</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#fixer'>Fixer</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#fan-of-knives'>Fan of Knives</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#imposing-presence'>Imposing Presence</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#jutsu-master'>Jutsu Master</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#leader'>Leader</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#protector'>Protector</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#single-handed-seals'>Single-Handed Seals</a>", unsafe_allow_html=True)
twoup.markdown("<a href='#skirmisher'>Skirmisher</a>", unsafe_allow_html=True)

twomd = open("phb/md/twoup.md", "r")
twoup.write(twomd.read())

threeup.markdown("<a href='#regenerative-chakra'>Regenerative Chakra</a>", unsafe_allow_html=True)
threeup.markdown("<a href='#relentless'>Relentless</a>", unsafe_allow_html=True)
threeup.markdown("<a href='#surging-power'>Surging Power</a>", unsafe_allow_html=True)
threeup.markdown("<a href='#tactician'>Tactician</a>", unsafe_allow_html=True)

threemd = open("phb/md/threeup.md", "r")
threeup.write(threemd.read())
