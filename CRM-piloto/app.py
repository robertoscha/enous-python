import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_searchbox import st_searchbox



def search_clientes(query):
    return [c for c in clientes if query.lower() in c.lower()]

clientes = ["Cliente A", "Cliente B", "Cliente C"]
vendedores = ["Vendedor X", "Vendedor Y", "Vendedor Z"]

st.title("Registro de contactos")
# st.caption("Cliente")
st.markdown("Cliente")
cliente = st_searchbox(search_clientes, key="cliente", placeholder="Buscar cliente")
vendedor = st.selectbox("Vendedor", vendedores)
tipo = st.selectbox("Tipo de contacto", ["Llamada", "WhatsApp", "Visita"])

if st.button("Guardar"):
    nuevo = pd.DataFrame([[datetime.now(), cliente, vendedor, tipo]],
                         columns=["Fecha", "Cliente", "Vendedor", "Tipo"])
    try:
        df = pd.read_excel("contactos.xlsx")
        df = pd.concat([df, nuevo], ignore_index=True)
    except FileNotFoundError:
        df = nuevo
    df.to_excel("contactos.xlsx", index=False)
    st.success("Contacto guardado")