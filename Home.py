import streamlit as st
import base64

st.set_page_config(
    page_title="Onta pokemon?",
    page_icon="🔅"
)

st.markdown("<h1 style='text-align: center; color: grey;'>¿Qué Pokémon Buscas?</h1>", unsafe_allow_html=True)

# Columnas y tabs de posición
tab_ruta, tab_pok = st.tabs(["Ruta", "Pokémon"])

with tab_ruta:
    
    nombre_ruta = st.text_input('Buscador de ruta por nombre')
    st.text(nombre_ruta)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_ruta)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')


