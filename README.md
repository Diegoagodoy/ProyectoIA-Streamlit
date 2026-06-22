# Proyecto Final – PresupuestoIA 🏗️

## 🚀 Accesos

### Aplicación Web

🔗 https://proyectoia-appgit-efg9hqul8zazw2fax38jp6.streamlit.app/

### 🎥 Video Demostrativo

🔗 https://drive.google.com/file/d/1QmwMDucdUJ3Qcr0vyYMHcEaDZRijHsdR/view?usp=drive_link

### 📊 Presentación del Proyecto

📄 Proyecto Final -PresupuestoIA- Godoy Diego Adolfo.pptx

### 📁 Carpeta de Entrega

🔗 https://drive.google.com/drive/folders/1KtJG71k2xLKiRR8BLafdfyqXoFwi9D1-?usp=sharing

---

## Descripción

PresupuestoIA es una aplicación web desarrollada en Python utilizando Streamlit e Inteligencia Artificial para generar estimaciones orientativas de costos de construcción.

La herramienta permite al usuario ingresar características básicas de un proyecto y obtener un análisis generado por IA que incluye una estimación económica, una justificación de los costos y recomendaciones constructivas.

Este proyecto tiene como objetivo demostrar la integración de modelos de lenguaje en aplicaciones web para asistir en la toma de decisiones dentro del ámbito de la construcción.


## Funcionalidades

* Selección del tipo de obra.
* Ingreso de superficie en metros cuadrados.
* Selección de provincia.
* Selección del nivel de terminaciones.
* Generación automática de una estimación orientativa mediante IA.
* Recomendaciones constructivas y de eficiencia energética.
* Interfaz web simple e intuitiva desarrollada con Streamlit.

---

## Tecnologías Utilizadas

* Python
* Streamlit
* OpenRouter API
* GPT
* Requests

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Diegoagodoy/ProyectoIA-Streamlit.git
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear el archivo:

```text
.streamlit/secrets.toml
```

Con el siguiente contenido:

```toml
API_KEY="TU_API_KEY"
```

---

## Ejecución

```bash
streamlit run test.py
```

---

## Uso

1. Seleccionar el tipo de obra.
2. Ingresar la superficie.
3. Seleccionar la provincia.
4. Elegir el nivel de terminaciones.
5. Presionar **Generar Análisis IA**.
6. Revisar el informe generado.

---

## Limitaciones

Los resultados obtenidos son estimaciones orientativas generadas mediante Inteligencia Artificial y no constituyen un presupuesto ejecutivo profesional.

---

## Autor

**Diego A. Godoy**

Proyecto Final – Diplomatura en Data Science e Inteligencia Artificial.

