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

def diag(punto):
    res = []
    res.append(punto[0])
    res.append([punto[0][0],punto[1][1]])
    res.append(punto[1])
    res.append([punto[1][0],punto[0][1]])
    return res
    
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
    
    # st.image('./mapa.png')

    map_file = open(f"./hoenn_json.json")
    map_data = json.load(map_file)

    imdata = base64.b64decode(map_data["imageData"])
    npimg = np.frombuffer(imdata, dtype=np.uint8);
    image = cv2.imdecode(npimg, 1)
    color = (255,0,0)
    
    for shape in map_data["shapes"]:
        if shape["label"] == location:
            pt = diag(shape["points"])
            pt = np.array(pt, np.int32)
            image_pol = cv2.fillPoly(image, [pt], color)
            cv2.imwrite(r"./poly.png",image_pol)
            cv2.imwrite(r"./empty.png",image_pol)
            
            frames_pop = []
            for i in ["./empty.png","./poly.png"]:
                new_frame_pop = Image.open(i)
                frames_pop.append(new_frame_pop)
    
            frames_pop[0].save('./png_to_gif.gif', format='GIF',
                       append_images=frames_pop[1:],
                       save_all=True,
                       duration=20, loop=0)
            
            file_ = open("./png_to_gif.gif", "rb")
            contents4 = file_.read()
            data_url4 = base64.b64encode(contents4).decode("utf-8")
            file_.close()
            st.markdown(f'<img src="data:image/gif;base64,{data_url4}" width="720" height="400" alt="gif">',
                                                unsafe_allow_html=True)
   

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_pok)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')
        

    


