import streamlit as st
import random

# Kompaktna nastavitev
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    /* Poravnavanje gumba na desno in naslova na levo */
    .stButton {display: flex; justify-content: flex-end;}
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

# Vrstica z naslovom in gumbom
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("### Алфавит")

with c2:
    label = "Покажи карточку" if st.session_state.prikazana_slika is None else "Следующая"
    if st.button(label):
        izberi_novo()
        st.rerun()

# Slika - poravnana pod njima
if st.session_state.prikazana_slika is not None:
    st.image(st.session_state.prikazana_slika, use_container_width=True)