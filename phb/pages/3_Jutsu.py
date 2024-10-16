import streamlit as st

jutsu = open("phb/md/Jutsu.md", "r")
st.write(jutsu.read())