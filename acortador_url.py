import pyshorteners #Libreria para acortar URLS
import streamlit as st # Libreria para crear pagina web.

#CREA UNA FUNCION PARA ACORTAR URL

def short_url(url): # crea funcion,le paso un input para url que queramos cortar.
    objeto = pyshorteners.Shortener()  #Crea un objeto de pyshortener
    acortar_url = objeto.tinyurl.short(url)  #LLama al metodo que acorta a la url.
    return acortar_url  #Devuelvo la url acortada.

#CREA APP WEB CON STREAMLIT

st.set_page_config(page_title="Acortador de URLS",page_icon="🖊️" ,layout="centered")#Configuramos la pagina,le damos titulo,icono y centralizamos la pagina
st.image("images/imagen_url.jpg",use_container_width= True) #Le da una imagen.
st.title("Acortador de URL") #Le da titulo
url = st.text_input("Ingrese la url") # Se crea un text input para ingresar la url que queremos cortar.
if st.button("Generar URL"): #Crea una condicional con un boton para generar la url.
    st.write("URL acortada: "), short_url(url) #Si se pulsa genera la url acortada.