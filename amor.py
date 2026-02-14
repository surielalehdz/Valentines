import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
from datetime import date

# --- 1. CONFIGURACIÓN Y ESTILO (OPTIMIZADO PARA MÓVIL) ---
st.set_page_config(page_title="Para Daniela ❤️", page_icon="💖", layout="wide")

# Fecha de inicio
FECHA_INICIO = date(2025, 8, 20) 
dias_juntos = (date.today() - FECHA_INICIO).days

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #ffe4e1;
        background-image: url("https://www.transparenttextures.com/patterns/hearts.png");
    }}
    /* Título más grande y con sombra para que resalte */
    .titulo {{
        font-size: 42px !important;
        font-weight: 800;
        color: #b00020; /* Un rojo más fuerte para lectura */
        text-align: center;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
        margin-bottom: 5px;
    }}
    /* Texto del contador en color oscuro */
    .contador {{
        font-size: 20px;
        color: #5d001e;
        text-align: center;
        margin-bottom: 30px;
        font-weight: 600;
    }}
    /* Ajuste de las tarjetas para que el texto adentro sea legible */
    .card {{
        background: rgba(255, 255, 255, 0.95); /* Blanco sólido */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: #1a1a1a !important; /* Texto casi negro para máximo contraste */
        line-height: 1.6; /* Espaciado entre líneas */
    }}
    /* Forzar color negro en las listas de col2 */
    .stMarkdown p, .stMarkdown li {{
        color: #1a1a1a !important;
        font-size: 17px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

def load_lottieurl(url):
    try:
        return requests.get(url).json()
    except: return None

lottie_love = load_lottieurl("https://lottie.host/8074d093-5961-460d-9659-380d6b63d0c3/9S0nNf1N63.json")

# --- LÓGICA DE NAVEGACIÓN ---
if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- PANTALLA 1: LA PROPUESTA ---
if st.session_state.paso == 1:
    st.markdown('<p class="titulo">Daniela de mi corazón,<br>¿Quieres ser mi San Valentín mañana?</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="contador">Llevamos {dias_juntos} días de aprendizaje y amor...</p>', unsafe_allow_html=True)
    
    # Botón centrado
    st.markdown('<div class="centrar">', unsafe_allow_html=True)
    if st.button("¡SÍ, ACEPTO! ❤️"):
        st.balloons()
        time.sleep(1)
        st.session_state.paso = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PANTALLA 2: EL PANEL ROMÁNTICO ---
else:
    st.markdown('<p class="titulo">¡Mañana es nuestro día! 😍</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎵 Nuestra canción")
        st.video("https://www.youtube.com/watch?v=oSpT9pNyoBI") 
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("💌 Mensaje Secreto")
        with st.expander("Haz clic para leer..."):
            st.write("Amor, feliz día. Sé que hemos pasado por momentos difíciles últimamente, pero te sigo eligiendo hoy y todos los días. Gracias por querer luchar por lo nuestro junto a mí. Hagamos que este día sea un recordatorio de por qué empezamos y de todo lo bueno que nos falta vivir. Te quiero mucho")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎥 Un video para ti")
        try:
            # Carga del video local que pusiste en la carpeta
            video_file = open('mi_video.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
        except:
            st.warning("Coloca tu video 'mi_video.mp4' en la carpeta para verlo aquí ❤️")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("❤️ ¿Por qué me gustas?")
        st.write(f"En estos {dias_juntos} días he aprendido que:")
        st.write("* Tus abrazos son mi lugar favorito.")
        st.write("* Nadie me hace reír como tú.")
        st.write("* Eres mi apoyo incondicional.")
        st.write("* Te deseo.")
        st.write("* Eres la mamá de Rayo jaja.")
        st.write("* No dejo de pensar en ti.")
        st.write("* Quiero ser feliz contigo :).")
        st.markdown('</div>', unsafe_allow_html=True)
        
    if lottie_love:
        st_lottie(lottie_love, height=200)

    st.markdown(f"<h3 style='text-align: center; color: #d11141;'>¡Nos vemos mañana para celebrar el día {dias_juntos + 1}!</h3>", unsafe_allow_html=True)
