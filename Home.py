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
    with open("encounters.json", "r") as file:
        encounters = json.load(file)
        if nombre_ruta != "":
            try:
                resultados = encounters["lugares"][0][nombre_ruta][0]
                for tipo in resultados:
                    n = 0
                    res = resultados[tipo]
                    st.subheader(tipo.upper().replace("-"," "))
                    col1, col2, col3, col4, col5 = st.columns(5)
                    columnas = [col1, col2, col3, col4, col5]
                    for pok in res:
                        with columnas[n%5]:
                            st.text(list(pok.keys())[0])
                            st.text(list(pok.values())[0])
                            funciones.get_sprite(list(pok.keys())[0])
                            file_ = open("spriteGIF.gif", "rb")
                            contents = file_.read()
                            data_url = base64.b64encode(contents).decode("utf-8")
                            file_.close()
                            dim = Image.open("spriteGIF.gif").size
                            w = dim[0] * 1.8
                            h = dim[1] * 1.8
                            st.markdown(f'<img src="data:image/gif;base64,{data_url}"  width={w} height={h} alt="cat gif">',
                                            unsafe_allow_html=True)
                            n += 1
            except:
                st.text("Nombre de ruta incorrecto")
   

with tab_pok:
    
    nombre_pok = st.text_input('Buscador de Pokémon por nombre')
    st.text(nombre_pok)
    
    col1, col2 = st.columns(2)
    with col2:
        st.image('./mapa.png')
        

    


