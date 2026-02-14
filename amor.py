import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
from datetime import date

# --- 1. CONFIGURACIÓN Y ESTILO (ESTILO ORIGINAL RECUPERADO) ---
st.set_page_config(page_title="Para Daniela ❤️", page_icon="💖", layout="wide")

FECHA_INICIO = date(2025, 8, 20) 
dias_juntos = (date.today() - FECHA_INICIO).days

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #ffe4e1;
        background-image: url("https://www.transparenttextures.com/patterns/hearts.png");
    }}
    
    /* Títulos Principales en Rojo */
    .titulo {{
        font-size: 40px !important;
        font-weight: bold;
        color: #d11141;
        text-align: center;
        margin-bottom: 0px;
    }}
    
    .contador {{
        font-size: 18px;
        color: #8b0000;
        text-align: center;
        margin-bottom: 30px;
        font-style: italic;
    }}

    /* Botón a la izquierda (según tu captura) */
    div.stButton > button {{
        background-color: #ff1493 !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 10px 30px !important;
        border-radius: 30px !important;
        border: 2px solid white !important;
    }}

    /* Tarjetas Blancas con Títulos Rojos */
    .card {{
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }}

    /* Títulos de las tarjetas en rojo/rosa fuerte */
    .card-title {{
        color: #d11141;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }}

    /* Texto interno legible pero sutil */
    .card-text {{
        color: #333333;
        font-size: 16px;
        line-height: 1.4;
    }}
    </style>
    """, unsafe_allow_html=True)

def load_lottieurl(url):
    try: return requests.get(url).json()
    except: return None

lottie_love = load_lottieurl("https://lottie.host/8074d093-5961-460d-9659-380d6b63d0c3/9S0nNf1N63.json")

if 'paso' not in st.session_state:
    st.session_state.paso = 1

# --- PANTALLA 1: LA PROPUESTA ---
if st.session_state.paso == 1:
    st.markdown('<p class="titulo">Daniela de mi corazón,</p>', unsafe_allow_html=True)
    st.markdown('<p class="titulo">¿Quieres ser mi San Valentín mañana?</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="contador">Llevamos {dias_juntos} días de aprendizaje y amor...</p>', unsafe_allow_html=True)
    
    # Botón a la izquierda como en tu imagen
    if st.button("¡SÍ, ACEPTO! ❤️"):
        st.balloons()
        time.sleep(1)
        st.session_state.paso = 2
        st.rerun()

# --- PANTALLA 2: EL PANEL ROMÁNTICO (COMO LA IMAGEN) ---
else:
    st.markdown('<p class="titulo">¡Mañana es nuestro dia! 😍</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎵 Nunca la olvides")
        st.write("Canciones que me recuerdan a ti:")
        # Puedes poner un link real de Spotify o YouTube aquí
        st.video("https://www.youtube.com/watch?v=oSpT9pNyoBI&list=RDoSpT9pNyoBI&start_radio=1") 
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("💌 Mensaje Secreto")
        with st.expander("Haz clic para leer..."):
            st.write("Amor, feliz día. Sé que hemos pasado por momentos difíciles últimamente, pero te sigo eligiendo hoy y todos los días. Gracias por querer luchar por lo nuestro junto a mí. Hagamos que este día sea un recordatorio de por qué empezamos y de todo lo bueno que nos falta vivir. Te quiero mucho")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("❤️ ¿Por qué me gustas?")
        st.write(f"En estos {dias_juntos} días he aprendido que:")
        st.write("* Tus abrazos son mi lugar favorito.")
        st.write("* Nadie me hace reír como tú.")
        st.write("* Eres mi apoyo incondicional.")
        st.write("* Te deseo.")
        st.write("* Eres la mamá de Rayo jaja.")
        st.write("* No dejo de pensar en ti.")
        st.write("* Quiero ser feliz contigo:).")
        st.write("* Tenemos una historia por escribir juntos.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if lottie_love:
            st_lottie(lottie_love, height=200)

    st.markdown(f"<h3 style='text-align: center; color: #d11141;'>¡Nos vemos mañana para celebrar el día {dias_juntos + 1}!</h3>", unsafe_allow_html=True)
