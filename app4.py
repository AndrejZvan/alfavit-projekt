import streamlit as st
import random

# Kompaktna postavitev
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    /* Naslov in gumbi v isti liniji */
    .row-widget.stButton { margin-top: 0px; }
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

# Vodoravna postavitev: Gumb - Naslov - Gumb
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.prikazana_slika is None:
        if st.button("Покажи"): # Malo krajše ime za prostor
            izberi_novo()
            st.rerun()
    else:
        if st.button("Следующая"):
            izberi_novo()
            st.rerun()

with col2:
    st.markdown("<h3 style='text-align: center; margin-top: 0px;'>Алфавит</h3>", unsafe_allow_html=True)

with col3:
    st.write("") # Prazno za ravnotežje

# Slika spodaj
if st.session_state.prikazana_slika is not None:
    st.image(st.session_state.prikazana_slika, use_container_width=True)