
# data_loader.py
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

@st.cache_data
def cargar_datos():
    # Crea el string de conexión
    conn_str = (
        "mssql+pyodbc://eNousProt:OttoFona0707.-@192.168.0.202/eNous"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    # Crea el engine de SQLAlchemy
    engine = create_engine(conn_str)

    query = """SELECT c.ClteCd codigo_cliente, c.ClteNm nombre_cliente
    FROM eNous.dbo.Clte c"""

    return pd.read_sql(query, engine)


