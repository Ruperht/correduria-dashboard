import pandas as pd

def prima_total(df: pd.DataFrame) -> float:
    return df["prima_anual"].sum()

def total_polizas(df: pd.DataFrame) -> int:
    return len(df)

def ratio_cancelacion(df: pd.DataFrame) -> float:
    canceladas = (df["estado_poliza"] == "Cancelada").sum()
    return round((canceladas / len(df)) * 100, 1) if len(df) > 0 else 0.0

def cartera_por_aseguradora(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("aseguradora")["prima_anual"]
        .sum()
        .reset_index()
        .sort_values("prima_anual", ascending=False)
    )

def polizas_por_tipo(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("tipo_poliza")
        .size()
        .reset_index(name="total")
        .sort_values("total", ascending=False)
    )

def altas_por_mes(df: pd.DataFrame) -> pd.DataFrame:
    temp = df.copy()
    temp["mes_alta"] = temp["fecha_alta"].dt.to_period("M").astype(str)
    return (
        temp.groupby("mes_alta")
        .size()
        .reset_index(name="total")
        .sort_values("mes_alta")
    )

def polizas_por_canal(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("canal_captacion")
        .size()
        .reset_index(name="total")
        .sort_values("total", ascending=False)
    )