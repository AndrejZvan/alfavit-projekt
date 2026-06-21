import streamlit as st
import random

# Nastavitev strani na "wide" in skritje menija
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# CSS: Skrijemo zgornji meni in zmanjšamo vse odmike na nulo
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 1rem; padding-right: 1rem;}
    h1 {font-size: 1.5rem !important; margin-bottom: 0.5rem !important; text-align: center;}
    .stImage {max-height: 60vh !important; display: flex; justify-content: center;}
    </style>
    """, unsafe_allow_html=True)

def nalozi_povezave():
    try:
        with open("povezave.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except: return []

url_seznama = nalozi_povezave()

if 'prikazana_slika' not in st.session_state:
    st.session_state.prikazana_slika = None

def izberi_novo():
    if url_seznama: st.session_state.prikazana_slika = random.choice(url_seznama)

# Vsebina
st.title("Алфавит")

if st.session_state.prikazana_slika is None:
    if st.button("Покажи карточку"):
        izberi_novo()
        st.rerun()
else:
    # Slika je omejena na 60% višine zaslona, da ostane prostor za gumb
    st.image(st.session_state.prikazana_slika)
    if st.button("Следующая"):
        izberi_novo()
        st.rerun()