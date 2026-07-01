import plotly.express as px
import pandas as pd

def grafico_altas_por_mes(df: pd.DataFrame):
    fig = px.line(
        df,
        x="mes_alta",
        y="total",
        title="Evolución de altas por mes",
        labels={"mes_alta": "Mes", "total": "Nº de altas"},
        markers=True
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def grafico_polizas_por_tipo(df: pd.DataFrame):
    fig = px.bar(
        df,
        x="tipo_poliza",
        y="total",
        title="Pólizas por tipo de seguro",
        labels={"tipo_poliza": "Tipo", "total": "Nº de pólizas"},
        color="tipo_poliza"
    )
    return fig

def grafico_cartera_aseguradora(df: pd.DataFrame):
    fig = px.bar(
        df,
        x="aseguradora",
        y="prima_anual",
        title="Prima total por aseguradora",
        labels={"aseguradora": "Aseguradora", "prima_anual": "Prima total (€)"},
        color="aseguradora"
    )
    return fig

def grafico_canal_captacion(df: pd.DataFrame):
    fig = px.pie(
        df,
        names="canal_captacion",
        values="total",
        title="Distribución por canal de captación"
    )
    return fig