import streamlit as st
import base64
import json
import funciones
import pandas as pd
import numpy as np
import cv2
import base64
import imageio as iio
from PIL import Image

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

    map_file = open(f"./hoenn_json.json")
    map_data = json.load(map_file)

    imdata = base64.b64decode(map_data["imageData"])
    npimg = np.frombuffer(imdata, dtype=np.uint8);
    image = cv2.imdecode(npimg, 1)
    color = (100,0,220)
    
    for shape in map_data["shapes"]:
        if shape["label"] == location:
            pt = np.array(shape["points"], np.int32)
            image = cv2.fillPoly(image, [pt], color)
            st.image(image)
   

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_pok)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')
        

    


