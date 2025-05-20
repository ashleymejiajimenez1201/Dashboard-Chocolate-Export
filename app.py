import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurar estilo pastel suave
plt.style.use('seaborn-pastel')

# URLs de los archivos CSV con tu usuario de GitHub
clientes_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/barreras.csv"

# Cargar datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Título
st.title("🍫 Dashboard Interactivo de Exportaciones de Chocolates")

# Selección país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("🌍 Selecciona un país", sorted(paises))

# Clientes
st.subheader("👥 Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Exportaciones - gráfico de pastel
st.subheader("📦 Distribución de Exportaciones por Producto")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
if not exportaciones_filtradas.empty:
    fig1, ax1 = plt.subplots()
    ax1.pie(
        exportaciones_filtradas["Exportaciones (USD millones)"],
        labels=exportaciones_filtradas["Producto"],
        autopct='%1.1f%%',
        startangle=140,
        colors=["#F7DC6F", "#F5B7B1", "#A9CCE3", "#F9E79F", "#D7BDE2"]
    )
    ax1.axis("equal")
    st.pyplot(fig1)
else:
    st.info("No hay datos de exportaciones para este país.")

# Segmentos de mercado
st.subheader("📊 Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Gráfico pastel tamaños de mercado
if not mercados_filtrados.empty:
    st.subheader("🧁 Distribución del Tamaño del Mercado por Segmento")
    fig2, ax2 = plt.subplots()
    ax2.pie(
        mercados_filtrados["Tamaño del Mercado (USD millones)"],
        labels=mercados_filtrados["Segmento"],
        autopct='%1.1f%%',
        startangle=140,
        colors=["#FAD7A0", "#F5CBA7", "#D2B4DE", "#AED6F1"]
    )
    ax2.axis("equal")
    st.pyplot(fig2)
else:
    st.info("No hay información de segmentos de mercado para este país.")

# Barreras de entrada
st.subheader("🚧 Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Comparación global
st.subheader("🌎 Comparación Global de Tamaños de Mercado")
top_mercados = mercados.groupby("País")["Tamaño del Mercado (USD millones)"].sum().nlargest(5)
fig3, ax3 = plt.subplots()
ax3.pie(
    top_mercados.values,
    labels=top_mercados.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=["#F7C6C7", "#F9E79F", "#A3E4D7", "#D7BDE2", "#EDBB99"]
)
ax3.axis("equal")
st.pyplot(fig3)
