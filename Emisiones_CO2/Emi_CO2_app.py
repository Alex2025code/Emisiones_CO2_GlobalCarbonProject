import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard Emisiones CO2",
    page_icon="🌍",
    layout="wide"
)
# -------------------------
# Título
# -------------------------

st.title("🌍 Dashboard de emisiones CO2")
st.write("Análisis de emisiones usando datos del Global Carbon Project")

# -------------------------
# Cargar dataset
# -------------------------

@st.cache_data
def load_data(): 
    
    df = pd.read_csv("GCB2022v27_MtCO2_flat.csv")

# Limpieza básica de datos
    df = df.dropna(subset=["Country"])
    df = df[~df["Country"].isin([
    "World",
    "Asia",
    "Europe",
    "International Transport"
    ])]
    
    return df
df = load_data()
#---------------------------
# convertir años a entero
#---------------------------
df["Year"] = df["Year"].astype(int)

# rellenar valores faltantes en fuentes de emisión
sources = ["Coal","Oil","Gas","Cement","Flaring"]
df[sources] = df[sources].fillna(0)

# -------------------------
# Indicadores globales
# -------------------------

st.subheader("📊 Indicadores globales")

col1, col2, col3 = st.columns(3)

col1.metric("Total países analizados", df["Country"].nunique())
col2.metric("Año inicial", df["Year"].min())
col3.metric("Año final", df["Year"].max())

#--------------------------
# 🌍 Mapa mundial de emisiones de CO2
#--------------------------

st.subheader("🌍 Mapa mundial de emisiones de CO2") 

year_map = st.slider( "Selecciona el año para el mapa", 
    int(df["Year"].min()), 
    int(df["Year"].max()), 
    2020 ) 
df_map = df[df["Year"] == year_map] 

fig_map = px.choropleth( 
    df_map, locations="Country",
    locationmode="country names", 
    color="Total", hover_name="Country", 
    color_continuous_scale="Reds", 
    title=f"Emisiones de CO2 por país en {year_map}" 
    ) 

st.plotly_chart(fig_map, use_container_width=True)

#---------------------------
"""
col1, col2 = st.columns(2)

# MAPA
with col1:

 st.subheader("🌍 Mapa mundial de emisiones de CO2")
 
 year_map = st.slider(
    "Selecciona el año para el mapa",
    int(df["Year"].min()),
    int(df["Year"].max()),
    2020
)

df_map = df[df["Year"] == year_map]

fig_map = px.choropleth(
    df_map,
    locations="Country",
    locationmode="country names",
    color="Total",
    hover_name="Country",
    color_continuous_scale="Reds",
    title=f"Emisiones de CO2 por país en {year_map}"
)

st.plotly_chart(fig_map, use_container_width=True)

# Top Emisores
with col2:

    st.subheader("Top países emisores")

    year = st.slider(
        "Selecciona año",
        int(df["Year"].min()),
        int(df["Year"].max()),
        2020,
        key="top_year"
    )

    df_year = df[df["Year"] == year]

    top10 = df_year.sort_values(
        "Total",
        ascending=False
    ).head(10)

    fig2 = px.bar(
        top10,
        x="Country",
        y="Total",
        title=f"Top 10 emisores en {year}"
    )

    st.plotly_chart(fig2, use_container_width=True)"""
# -------------------------
# Seleccionar país
# -------------------------
st.subheader("🌍 Evolución emisiones de CO2 por país")

countries = df['Country'].unique()

country = st.selectbox(
    "Selecciona un país",
    sorted(countries)
)

df_country = df[df["Country"] == country]

# -------------------------
# Gráfico evolución CO2
# -------------------------

fig = px.line(
    df_country, 
    x="Year",
    y="Total",
    title=f"Evolución emisiones CO2 - {country}"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# Top emisores
# -------------------------

st.subheader("🌍 Top países emisores")

year = st.slider(
    "Selecciona un año",
    int(df.Year.min()),
    int(df.Year.max()),
    2020
)

df_year = df[df["Year"] == year]

top10 = df_year.sort_values(
    "Total",
    ascending=False
).head(10)

fig2 = px.bar(
    top10,
    x="Country",
    y="Total",
    title=f"Top 10 emisores de CO2 en {year}"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------
# Distribución global de emisiones por fuente
#---------------------------------------------
st.subheader("🧱 Distribución global de emisiones por fuente (1750-2021)")

sources = ["Coal", "Oil", "Gas", "Cement", "Flaring"]

source_totals = df[sources].sum()

df_sources = pd.DataFrame({
    "Fuente": sources,
    "Emisiones": source_totals.values
})

fig_sources = px.pie(
    df_sources,
    values="Emisiones",
    names="Fuente",
    title="Distribución global de emisiones por fuente"
)

st.plotly_chart(fig_sources, use_container_width=True)

# --------------------------------------------
# Evolución de emisiones por tipo de fuente
# --------------------------------------------
st.subheader("📊 Evolución de emisiones por tipo de fuente")

sources = ["Coal", "Oil", "Gas", "Cement", "Flaring"]

df_sources_time = df.groupby("Year")[sources].sum().reset_index()

df_melt = df_sources_time.melt(
    id_vars="Year",
    value_vars=sources,
    var_name="Fuente",
    value_name="Emisiones"
)

fig_trend = px.line(
    df_melt,
    x="Year",
    y="Emisiones",
    color="Fuente",
    title="Evolución de emisiones por fuente"
)

st.plotly_chart(fig_trend, use_container_width=True)
