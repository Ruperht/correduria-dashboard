import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from src.data_loader import cargar_datos
from src import kpis, charts

# ── Configuración de la página ──────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard Correduría",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Correduría de Seguros")

# ── Carga de datos ───────────────────────────────────────────────────────────
df = cargar_datos()

# ── Sidebar con filtros ──────────────────────────────────────────────────────
st.sidebar.header("Filtros")

tipos = ["Todos"] + sorted(df["tipo_poliza"].dropna().unique().tolist())
tipo_sel = st.sidebar.selectbox("Tipo de póliza", tipos)

aseguradoras = ["Todas"] + sorted(df["aseguradora"].dropna().unique().tolist())
aseg_sel = st.sidebar.selectbox("Aseguradora", aseguradoras)

estados = ["Todos"] + sorted(df["estado_poliza"].dropna().unique().tolist())
estado_sel = st.sidebar.selectbox("Estado de póliza", estados)

# ── Aplicar filtros ──────────────────────────────────────────────────────────
df_filtrado = df.copy()

if tipo_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo_poliza"] == tipo_sel]
if aseg_sel != "Todas":
    df_filtrado = df_filtrado[df_filtrado["aseguradora"] == aseg_sel]
if estado_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["estado_poliza"] == estado_sel]

# ── KPIs ─────────────────────────────────────────────────────────────────────
st.subheader("Resumen general")
col1, col2, col3 = st.columns(3)

col1.metric("Total pólizas", kpis.total_polizas(df_filtrado))
col2.metric("Prima total (€)", f"{kpis.prima_total(df_filtrado):,.2f} €")
col3.metric("Ratio cancelación", f"{kpis.ratio_cancelacion(df_filtrado)} %")

st.divider()

# ── Gráficos ─────────────────────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.plotly_chart(
        charts.grafico_polizas_por_tipo(kpis.polizas_por_tipo(df_filtrado)),
        use_container_width=True
    )

with col_b:
    st.plotly_chart(
        charts.grafico_cartera_aseguradora(kpis.cartera_por_aseguradora(df_filtrado)),
        use_container_width=True
    )

col_c, col_d = st.columns(2)

with col_c:
    st.plotly_chart(
        charts.grafico_altas_por_mes(kpis.altas_por_mes(df_filtrado)),
        use_container_width=True
    )

with col_d:
    st.plotly_chart(
        charts.grafico_canal_captacion(kpis.polizas_por_canal(df_filtrado)),
        use_container_width=True
    )