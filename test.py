import streamlit as st
import requests

st.set_page_config(
    page_title="PresupuestoIA",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ PresupuestoIA")
st.write("Generador de presupuestos orientativos mediante Inteligencia Artificial")

tipo_obra = st.selectbox(
    "Tipo de obra",
    [
        "Vivienda",
        "Local Comercial",
        "Oficina",
        "Galpón"
    ]
)

superficie = st.number_input(
    "Superficie (m²)",
    min_value=1
)

provincia = st.selectbox(
    "Provincia",
    [
        "Buenos Aires",
        "Córdoba",
        "Santa Fe",
        "Mendoza"
    ]
)

terminaciones = st.selectbox(
    "Nivel de terminaciones",
    [
        "Básico",
        "Estándar",
        "Premium"
    ]
)

API_KEY = st.secrets["API_KEY"]

def consultar_ia(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=data
        )

        resultado = response.json()

        return resultado["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


if st.button("Generar Análisis IA"):

    prompt = f"""
Actuá como un especialista en presupuestos de construcción de Argentina.

Necesito una estimación orientativa para:

Tipo de obra: {tipo_obra}
Superficie: {superficie} m²
Provincia: {provincia}
Nivel de terminaciones: {terminaciones}

Generá la respuesta con el siguiente formato:

## PRESUPUESTO ESTIMADO

Costo estimado por m²:
(Indicar valor aproximado en USD)

Costo total estimado:
(Indicar valor aproximado en USD)

## JUSTIFICACIÓN

Explicar brevemente cómo influye:
- La provincia
- El tipo de obra
- El nivel de terminaciones

## RECOMENDACIONES

- Consideraciones climáticas
- Riesgos constructivos
- Consejos de eficiencia energética

Aclarar que se trata de una estimación orientativa y no de un presupuesto ejecutivo.
"""

    with st.spinner("Analizando proyecto..."):
        respuesta = consultar_ia(prompt)

    st.success("Análisis generado")

    st.subheader("🤖 Recomendaciones IA")

    st.write(respuesta)