import streamlit as st
import random

# Nastavitev strani
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Agresiven CSS za popoln nadzor nad postavitvijo
st.markdown("""
    <style>
    /* Odstrani vse privzete odmike Streamlita na vrhu */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    
    /* Flexbox vrstica - prisili elemente v eno vrstico */
    .row-container {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
    }
    
    /* Gumb in naslov - brez marginov */
    h3 { margin: 0 !important; padding: 0 !important; font-size: 1.5rem !important; }
    .stButton { margin: 0 !important; padding: 0 !important; width: auto !important; }
    .stButton > button { padding: 4px 8px !important; font-size: 0.9rem !important; }
    
    /* Skrij elemente, ki jemljejo prostor */
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

# Izris glave v eni vrstici preko HTML
st.markdown('<div class="row-container">', unsafe_allow_html=True)
st.markdown("### Алфавит")

# Gumb za izbiro
label = "Начать" if st.session_state.prikazana_slika is None else "Дальше"
if st.button(label):
    izberi_novo()
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Prikaz slike
if st.session_state.prikazana_slika is not None:
    st.image(st.session_state.prikazana_slika, use_container_width=True)