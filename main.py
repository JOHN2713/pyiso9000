import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
# Configurar tu API KEY de Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# Inicializar modelo
model = genai.GenerativeModel("gemini-1.5-flash")



# Función para generar caso de estudio
def generar_caso_estudio():
    prompt = (
        "Genera un caso de estudio breve y original relacionado exclusivamente con la norma ISO 9000. "
        "Debe presentar una situación problemática realista en una organización que lidie con aspectos de gestión de calidad."
    )
    response = model.generate_content(prompt)
    return response.text.strip()

# Función para análisis tipo auditoría IA
def generar_auditoria_ia(caso_estudio):
    prompt = (
        f"Actúa como un auditor experto en ISO 9000. A continuación se presenta un caso de estudio:\n\n"
        f"{caso_estudio}\n\n"
        "Realiza un análisis tipo auditoría de acuerdo a la norma ISO 9000. Enfócate en detección de fallas, buenas prácticas y oportunidades de mejora."
    )
    response = model.generate_content(prompt)
    return response.text.strip()

# Función para comparar análisis humano vs IA
def comparar_auditorias(analisis_humano, auditoria_ia):
    prompt = (
        f"Comparar dos auditorías sobre un caso de estudio relacionado con ISO 9000.\n\n"
        f"Auditoría humana:\n{analisis_humano}\n\n"
        f"Auditoría IA:\n{auditoria_ia}\n\n"
        "Evalúa cuál es mejor y por qué. Luego crea una lista de 'Checkpoints' con aspectos en los que el análisis humano falló, "
        "y otros en los que superó al análisis de IA. Sé objetivo y constructivo."
    )
    response = model.generate_content(prompt)
    return response.text.strip()

# Interfaz Streamlit
st.set_page_config(page_title="Auditoría ISO 9000 con Gemini", layout="centered")

st.title("📋 Generador de Casos ISO 9000 + Auditoría con IA")

# Paso 1: Generar caso de estudio
if "caso_estudio" not in st.session_state:
    st.session_state.caso_estudio = ""
if "analisis_humano" not in st.session_state:
    st.session_state.analisis_humano = ""
if "auditoria_ia" not in st.session_state:
    st.session_state.auditoria_ia = ""
if "comparacion" not in st.session_state:
    st.session_state.comparacion = ""

if st.button("🎲 Generar Caso de Estudio ISO 9000"):
    st.session_state.caso_estudio = generar_caso_estudio()

if st.session_state.caso_estudio:
    st.subheader("Caso de Estudio Generado")
    st.markdown(st.session_state.caso_estudio)

    # Paso 2: Ingresar análisis humano
    st.subheader("✍ Tu análisis (tipo auditoría)")
    st.session_state.analisis_humano = st.text_area(
        "Escribe tu análisis aquí:", 
        value=st.session_state.analisis_humano, 
        height=200
    )

    # Paso 3: Generar auditoría IA
    if st.button("🤖 Generar Auditoría con IA"):
        st.session_state.auditoria_ia = generar_auditoria_ia(st.session_state.caso_estudio)

    if st.session_state.auditoria_ia:
        st.subheader("🔎 Auditoría IA")
        st.markdown(st.session_state.auditoria_ia)

    # Paso 4: Comparación
    if st.session_state.analisis_humano and st.session_state.auditoria_ia:
        if st.button("📊 Comparar Auditorías"):
            st.session_state.comparacion = comparar_auditorias(
                st.session_state.analisis_humano, 
                st.session_state.auditoria_ia
            )

    if st.session_state.comparacion:
        st.subheader("⚖ Comparación Final")
        st.markdown(st.session_state.comparacion)