import streamlit as st
import random

# Pripravimo stran, da je bolj kompaktna
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# CSS za zmanjšanje odmikov in fiksiranje višine
st.markdown("""
    <style>
    /* Odstrani privzeti top padding Streamlita */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    /* Naslov bolj kompakten */
    h1 { margin-top: -1rem; text-align: center; font-size: 2rem; }
    /* Gumbi na sredini */
    div.stButton { display: flex; justify-content: center; }
    </style>
    """, unsafe_allow_html=True)

def nalozi_povezave():
    try:
        with open("povezave.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except: return []

url_seznama = nalozi_povezave()

# Glavni del - brez nepotrebnih praznih stolpcev levo/desno
st.title("Алфавит")

if 'prikazana_slika' not in st.session_state:
    st.session_state.prikazana_slika = None

def izberi_novo():
    if url_seznama: st.session_state.prikazana_slika = random.choice(url_seznama)

if st.session_state.prikazana_slika is None:
    if st.button("Покажи карточку"):
        izberi_novo()
        st.rerun()
else:
    st.image(st.session_state.prikazana_slika, use_container_width=True)
    if st.button("Следующая"):
        izberi_novo()
        st.rerun()