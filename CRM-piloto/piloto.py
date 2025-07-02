import streamlit as st
import pandas as pd
from datetime import datetime

# Listas de ejemplo (puedes cargarlas desde un archivo si lo prefieres)
clientes = ["","Cliente A", "Cliente B", "Cliente C"]
vendedores = ["Vendedor X", "Vendedor Y", "Vendedor Z"]

st.title("Registro de contactos")

cliente = st.selectbox("Cliente", clientes,index=0)
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