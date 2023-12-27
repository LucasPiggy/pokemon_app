import streamlit as st
import base64

st.set_page_config(
    page_title="Onta pokemon?",
    page_icon="🔅"
)

st.markdown("<h1 style='text-align: center; color: grey;'>¿Qué Pokémon Buscas?</h1>", unsafe_allow_html=True)

st.selectbox('Selecciona un tipo', ["Water", "Grass", "Fire"], 
             index = None,
             placeholder = "Ningún tipo seleccionado")

# Columnas de posición
col1, col2 = st.columns(2)

nombre_ruta = st.text_input('Buscador de ruta por nombre')
st.text(nombre_ruta)

with col2:
    st.image('./mapa.png')


