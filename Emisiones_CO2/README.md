# 🌍 Dashboard de Emisiones de CO₂

Proyecto de análisis de emisiones de CO₂ utilizando datos del Global Carbon Project, incluyendo un dashboard interactivo desarrollado con Streamlit.
---

## 🌱 Contexto

El **dióxido de carbono (CO₂)** es el principal gas de efecto invernadero emitido por la actividad humana.  
Comprender su evolución histórica permite identificar patrones de desarrollo industrial, transiciones energéticas y los desafíos actuales del **cambio climático**.

El **Global Carbon Project (GCP)** es una iniciativa científica internacional dedicada a **cuantificar las emisiones y sumideros de carbono** a nivel global, con el fin de **apoyar políticas climáticas basadas en evidencia**.

🔗 **Fuente oficial del dataset:**  
[Global Carbon Project – CO₂ Emissions Dataset](https://www.globalcarbonproject.org/carbonbudget)

---
## 📊 Descripción

Este proyecto analiza las emisiones de dióxido de carbono (CO₂) a nivel global, explorando tendencias históricas, distribución por país y fuentes de emisión.

Incluye:

- Análisis exploratorio en Jupyter Notebook
- Dashboard interactivo en Streamlit

---

## 🚀 Funcionalidades del Dashboard

- 🌍 Mapa mundial de emisiones por país
- 📈 Evolución de emisiones por país
- 🏭 Top países emisores
- 🧱 Distribución de emisiones por fuente
- 📊 Evolución de emisiones por tipo de fuente

---

## 🛠 Tecnologías utilizadas

- Python
- Pandas
- Plotly
- Streamlit

---
## 📂 Estructura del proyecto
Emisiones_CO2/
│
├── Emi_CO2_app.py # Dashboard en Streamlit
├── Emi_CO2_pais.ipynb # Análisis exploratorio
├── README.md # Documentación principal
├── LICENSE
└── data/
└── GCB2022v27_MtCO2_flat.csv
---
---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:
   git clone https://github.com/Alex2025code/Emisiones_CO2_GlobalCarbonProject.git
3. Ir a la carpeta del proyecto:
   cd Emisiones_CO2
5. Ejecutar el Dashboard:
   streamlit run Emi_CO2_app.py

---
## 🔎 Resultados destacados

- Las emisiones globales se **multiplicaron exponencialmente** tras 1950.  
- **China y Estados Unidos** concentran la mayor parte de las emisiones acumuladas.  
- El **carbón** se mantiene como la principal fuente de emisiones CO₂, seguido por el **petróleo**, y en menor medida el **gas natural** pero en constante crecimiento.  
- Las fuentes **cement** y **flaring** tienen un aporte menor, aunque creciente desde los años 80.  
- Se observan **reducciones temporales** en periodos de crisis económicas globales.

---
## 🧠 Conclusión general

El análisis evidencia que el crecimiento de las emisiones de CO₂ está estrechamente ligado al desarrollo industrial y al modelo energético basado en combustibles fósiles. Aunque algunos países han logrado estabilizar sus emisiones, la tendencia global sigue siendo ascendente, lo que plantea grandes desafíos para la **transición hacia energías limpias** y la **cooperación internacional** frente al cambio climático.

---
📘 *Proyecto elaborado por **Alexis Ortiz Díaz***  
🎓 Ingeniero Industrial, Diplomado en Python & Data Science 
💡  Basado en datos del **Global Carbon Project (GCP)**
💼 Notebook desarrollado como práctica para portafolio profesional

---

