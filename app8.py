import streamlit as st
import random

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# CSS, ki ročno zgradi vodoravno vrstico
st.markdown("""
    <style>
    .header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 10px;
    }
    h3 { margin: 0 !important; }
    .stButton > button { margin: 0 !important; }
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

# Zgradimo vrstico ročno s HTML
label = "Покажи" if st.session_state.prikazana_slika is None else "Дальше"

st.markdown('<div class="header-row">', unsafe_allow_html=True)
st.markdown("### Алфавит")
# Gumb damo v posebno formo, da bo deloval
if st.button(label):
    izberi_novo()
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Slika
if st.session_state.prikazana_slika is not None:
    st.image(st.session_state.prikazana_slika, use_container_width=True)