import streamlit as st
import random

# Kompaktna nastavitev
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0.5rem; padding-bottom: 0rem;}
    
    /* Nasilna sila za eno vrstico */
    [data-testid="column"] {
        flex: 1 !important;
        flex-direction: row !important;
        display: flex !important;
        align-items: center !important;
    }
    
    /* Odstranitev vseh marginov */
    .stButton { margin: 0 !important; padding: 0 !important; }
    h3 { margin: 0 !important; padding: 0 !important; }
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

# Uporabimo manjši razpon za naslov, da ostane več prostora za gumb
c1, c2 = st.columns([1, 2]) 

with c1:
    st.markdown("### Алфавит")

with c2:
    label = "Покажи" if st.session_state.prikazana_slika is None else "Следующая"
    if st.button(label, use_container_width=True): # Dodan use_container_width
        izberi_novo()
        st.rerun()

# Slika - poravnana pod njima
if st.session_state.prikazana_slika is not None:
    st.image(st.session_state.prikazana_slika, use_container_width=True)