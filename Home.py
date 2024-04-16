import streamlit as st
import base64
import json
import funciones
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title="Onta pokemon?",
    page_icon="🔅"
)

st.markdown("<h1 style='text-align: center; color: grey;'>¿Qué Pokémon Buscas?</h1>", unsafe_allow_html=True)

tab_ruta, tab_pok = st.tabs(["Ruta", "Pokémon"])

with tab_ruta:
    data = pd.read_csv(r'./encountersCSV.csv',sep=";")
    # nombre_ruta = st.text_input('Buscador de ruta por nombre')
    loc_options = set(data["location"])
    location = st.selectbox("Select:",loc_options)

    search_res = data.loc[data["location"] == location]
    n_encounters = len(set(search_res["encounter"])) # Compruebas el num de encounters posibles (si hay pescando, tierra ... )
    
    st.table(search_res)
    
    st.image('./mapa.png')

    
   

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_pok)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')
        

    


