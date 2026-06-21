import streamlit as st
import random

# Funkcija za branje povezav
def nalozi_povezave():
    try:
        with open("povezave.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        st.error("Datoteka 'povezave.txt' ni najdena!")
        return []

url_seznama = nalozi_povezave()

# Sredinska poravnava za naslove
st.markdown("""
    <style>
    h1 {text-align: center;}
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("Алфавит")

    if 'prikazana_slika' not in st.session_state:
        st.session_state.prikazana_slika = None

    def izberi_novo():
        if url_seznama:
            st.session_state.prikazana_slika = random.choice(url_seznama)

    if st.session_state.prikazana_slika is None:
        # Ustvarimo tri pod-stolpce znotraj col2 za gumb
        sub1, sub2, sub3 = st.columns([1, 2, 1])
        with sub2:
            if st.button("Покажи карточку"):
                izberi_novo()
                st.rerun()
    else:
        st.image(st.session_state.prikazana_slika, use_container_width=True)
        # Ustvarimo tri pod-stolpce znotraj col2 za gumb
        sub1, sub2, sub3 = st.columns([1, 2, 1])
        with sub2:
            if st.button("Покажи новую карточку"):
                izberi_novo()
                st.rerun()