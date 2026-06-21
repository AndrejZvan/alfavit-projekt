import streamlit as st
import random

# Nastavitev strani
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Agresiven CSS za popoln nadzor
st.markdown("""
    <style>
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    .row-container {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
    }
    h3 { margin: 0 !important; padding: 0 !important; font-size: 1.5rem !important; }
    /* Gumb s puščico - fiksna velikost, da ne sili v novo vrsto */
    .stButton { margin: 0 !important; padding: 0 !important; width: auto !important; flex-shrink: 0 !important; }
    .stButton > button { padding: 4px 15px !important; font-size: 1.2rem !important; font-weight: bold !important; }
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
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
    if url_seznama: 
        st.session_state.prikazana_slika = random.choice(url_seznama)

# Izris glave
st.markdown('<div class="row-container">', unsafe_allow_html=True)
st.markdown("### Алфавит")

# Gumb s puščico namesto besedila
if st.button("→"):
    izberi_novo()
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Prikaz slike
if st.session_state.prikazana_slika is not None:
    st.image(st.session_state.prikazana_slika, use_container_width=True)