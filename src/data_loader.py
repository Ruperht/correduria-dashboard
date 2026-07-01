import pandas as pd
import streamlit as st
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "clientes_polizas.csv"

@st.cache_data
def cargar_datos() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)

    # Convertir fechas
    for col in ["fecha_alta", "fecha_vencimiento", "fecha_renovacion_real"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Limpiar primas negativas (dato sucio documentado)
    df = df[df["prima_anual"] >= 0].copy()

    return df