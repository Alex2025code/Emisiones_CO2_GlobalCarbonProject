# 🌍 Análisis de Emisiones Globales de CO₂ (GCB2022v27)

Este proyecto analiza la evolución histórica de las **emisiones de dióxido de carbono (CO₂)** a nivel global y por país, utilizando el dataset **GCB2022v27_MtCO2_flat.csv** publicado por el **Global Carbon Project (GCP)**.

El objetivo principal es comprender cómo han evolucionado las emisiones desde una perspectiva histórica, identificar los principales emisores y analizar los cambios en las fuentes de energía a lo largo del tiempo.

---

## 🌱 Contexto

El **dióxido de carbono (CO₂)** es el principal gas de efecto invernadero emitido por la actividad humana.  
Comprender su evolución histórica permite identificar patrones de desarrollo industrial, transiciones energéticas y los desafíos actuales del **cambio climático**.

El **Global Carbon Project (GCP)** es una iniciativa científica internacional dedicada a **cuantificar las emisiones y sumideros de carbono** a nivel global, con el fin de **apoyar políticas climáticas basadas en evidencia**.

🔗 **Fuente oficial del dataset:**  
[Global Carbon Project – CO₂ Emissions Dataset](https://www.globalcarbonproject.org/carbonbudget)

---

## 🎯 Objetivos del análisis

1. Realizar un **análisis exploratorio de datos (EDA)** para comprender la evolución global de las emisiones.  
2. Identificar a los **principales emisores históricos** y su evolución a lo largo del tiempo.  
3. Comparar las **fuentes de emisión** (carbón, petróleo, gas, etc.) y cómo ha cambiado su peso relativo.  
4. Analizar casos específicos de interés, como **China** y **Estados Unidos**, los dos mayores emisores actuales.  
5. Explorar visualizaciones avanzadas:
   - Series de tiempo globales.  
   - Gráficos por década.  
   - Correlaciones entre fuentes.  
   - Gráficos apilados y comparativos para mostrar la transición energética.

---

## 🧹 Tratamiento y análisis de datos

El notebook realiza los siguientes pasos:

- Carga y limpieza del dataset.
- Visualización de tendencias por tipo de fuente, periodo **1750-2021**.  
- Filtrado del periodo **1925–2021** (era industrial moderna).  
- Análisis descriptivo y exploratorio de las emisiones globales.  
- Visualización de tendencias por tipo de fuente (carbón, petróleo, gas, etc.).  
- Comparaciones entre países y períodos históricos.

---

## 📊 Visualizaciones principales

- **🌍 Evolución global de emisiones (1925–2021):** crecimiento casi exponencial desde mediados del siglo XX.  
- **📈 Distribución por fuente de emisión:** predominio del carbón y el petróleo, con aumento progresivo del gas.  
- **🇨🇳 vs 🇺🇸 Comparación China – EE.UU.:** transición del liderazgo en emisiones desde EE.UU. hacia China a partir de 2006.  
- **📉 Impactos históricos:** caídas puntuales en 1932 (Gran Depresión), 1973 (crisis del petróleo) y 2020 (pandemia).

---

## 🔎 Resultados destacados

- Las emisiones globales se **multiplicaron exponencialmente** tras 1950.  
- **China y Estados Unidos** concentran la mayor parte de las emisiones acumuladas.  
- El **carbón** se mantiene como la principal fuente de emisiones CO₂, seguido por el **petróleo**, y en menor medida el **gas natural** pero en constante crecimiento.  
- Las fuentes **cement** y **flaring** tienen un aporte menor, aunque creciente desde los años 80.  
- Se observan **reducciones temporales** en periodos de crisis económicas globales.

---

## 📁 Estructura del proyecto

---

## 🧠 Conclusión general

El análisis evidencia que el crecimiento de las emisiones de CO₂ está estrechamente ligado al desarrollo industrial y al modelo energético basado en combustibles fósiles. Aunque algunos países han logrado estabilizar sus emisiones, la tendencia global sigue siendo ascendente, lo que plantea grandes desafíos para la **transición hacia energías limpias** y la **cooperación internacional** frente al cambio climático.

---
📘 *Proyecto elaborado por **Alexis Ortiz Díaz***  
🎓 Ingeniero Industrial, Diplomado en Python & Data Science 
💡  Basado en datos del **Global Carbon Project (GCP)**
💼 Notebook desarrollado como práctica para portafolio profesional

---

