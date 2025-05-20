import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV (con tu usuario real)
clientes_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/ashleymejiajimenez1201/Dashboard-Chocolate-Export/main/barreras.csv"

# Cargar los datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
fig, ax = plt.subplots()
ax.bar(
    export
