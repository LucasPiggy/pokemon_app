import streamlit as st
import base64
import json

st.set_page_config(
    page_title="Onta pokemon?",
    page_icon="🔅"
)

st.markdown("<h1 style='text-align: center; color: grey;'>¿Qué Pokémon Buscas?</h1>", unsafe_allow_html=True)

# Columnas y tabs de posición
tab_ruta, tab_pok = st.tabs(["Ruta", "Pokémon"])

with tab_ruta:
    
    nombre_ruta = st.text_input('Buscador de ruta por nombre')

    with open("encounters.json", "r") as file:
        encounters = json.load(file)
        if nombre_ruta != "":
            try:
                resultados = encounters["lugares"][0][nombre_ruta][0]
                for tipo in resultados:
                    st.text(tipo)
                    st.text(resultados[tipo][0])
            except:
                st.text("Nombre de ruta incorrecto")
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_pok)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')


