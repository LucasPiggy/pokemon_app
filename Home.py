import streamlit as st
import base64
import json
import funciones
from PIL import Image

st.set_page_config(
    page_title="Onta pokemon?",
    page_icon="🔅"
)

st.markdown("<h1 style='text-align: center; color: grey;'>¿Qué Pokémon Buscas?</h1>", unsafe_allow_html=True)

# Columnas y tabs de posición
tab_ruta, tab_pok = st.tabs(["Ruta", "Pokémon"])

with tab_ruta:
    
    nombre_ruta = st.text_input('Buscador de ruta por nombre')
    
    col1, col2 = st.columns(2)

    with col1:
        with open("encounters.json", "r") as file:
            encounters = json.load(file)
            if nombre_ruta != "":
                try:
                    resultados = encounters["lugares"][0][nombre_ruta][0]
                    for tipo in resultados:
                        st.text(tipo)
                        res = resultados[tipo][0]
                        for pok in res:
                            st.text(pok)
                            funciones.get_sprite(pok)
                            st.text("Hola")
                            file_ = open("spriteGIF.gif", "rb")
                            contents = file_.read()
                            data_url = base64.b64encode(contents2).decode("utf-8")
                            file_.close()
                            dim = Image.open("spriteGIF.gif").size
                            w = dim[0] * 1.8
                            h = dim[1] * 1.8
                            st.markdown(f'<img src="data:image/gif;base64,{data_url}"  width={w} height={h} alt="cat gif">',
                                        unsafe_allow_html=True)
                except:
                    st.text("Nombre de ruta incorrecto")
    
    with col2:
        st.image('./mapa.png')

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_pok)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')


