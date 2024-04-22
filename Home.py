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
    location = st.selectbox("Selecciona una ruta:",loc_options)

    search_res = data.loc[data["location"] == location]
    n_encounters = len(set(search_res["encounter"])) # Compruebas el num de encounters posibles (si hay pescando, tierra ... )

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
                       duration=1000, loop=0)
            
            file_ = open("./png_to_gif.gif", "rb")
            contents4 = file_.read()
            data_url4 = base64.b64encode(contents4).decode("utf-8")
            file_.close()
            st.markdown(f'<img src="data:image/gif;base64,{data_url4}" width="720" height="400" alt="gif">',
                                                unsafe_allow_html=True)

    for encounter in ["land","old-rod","good-rod","super-rod","any-rod"]:
        search = search_res.loc[search_res["encounter"] == encounter]
        pok_res = set(search["pokemon"])
        search_n = len(search)
        if search_n != 0:
            exp = st.expander(f"{encounter} ({search_n})")
    
            with exp:
                col1, col2, col3, col4, col5 = st.columns(5)
                cols = [col1, col2, col3, col4, col5]
                n = 0
                for pok in pok_res:
                    with cols[n%5]:
                        st.text(pok)
                        funciones.get_sprite(pok)
                        file_ = open("./spriteGIF.gif", "rb")
                        contents4 = file_.read()
                        data_url4 = base64.b64encode(contents4).decode("utf-8")
                        file_.close()
                        st.markdown(f'<img src="data:image/gif;base64,{data_url4}" width="70" height="70" alt="gif">',
                                                            unsafe_allow_html=True)
                        prob = int(search.loc[search["pokemon"] == pok]["prob"])
                        tipos = funciones.get_tipo(pok)
                        for i in tipos:
                            st.image(Image.open(f'./tipos/{i}.png'), width = 75)
                        if len(tipos) == 1:
                            st.text("")
                            st.text("")
                        st.text(f"{prob}%")
                    n += 1
            
           

with tab_pok:
    data = pd.read_csv(r'./encountersCSV.csv',sep=";")
    tipos = set(data["tipo1"].dropna()).union(set(data["tipo2"].dropna()))
    caja_tipo = st.selectbox("Selecciona un tipo:", tipos, placeholder="Selecciona un Tipo")
    pok_options = set(data.loc[(data["tipo1"] == caja_tipo) | (data["tipo2"] == caja_tipo)]["pokemon"])
    pokemon = st.selectbox("Selecciona un Pokémon:",pok_options, placeholder="Selecciona un Pokémon")

    results = data.loc[data["pokemon"] == pokemon]
    locations = results["location"]
    probs = results["prob"]
    types = results["encounter"]

    tipos_pok = results.reset_index()["tipo1"][0]
    st.text(tipos_pok)
    st.text(f"{tipo1},{tipo2}")

    col1, col2 = st.columns(2)

    with col1:
        st.text(f"¿Dónde encontrar a {pokemon}?")
        funciones.get_sprite(pokemon)
        file_ = open("./spriteGIF.gif", "rb")
        contents4 = file_.read()
        data_url4 = base64.b64encode(contents4).decode("utf-8")
        file_.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url4}" alt="gif">',
                                                            unsafe_allow_html=True)
        

    with col2:
        for loc, type, prob in zip(locations, types, probs):
            st.text(f"Lugar: {loc} \n¿Cómo?: {type} \nProb:{prob}% \n-----------------------------------------")
            
        

    


