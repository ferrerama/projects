import marimo

__generated_with = "0.16.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    from pandas.api.types import CategoricalDtype


    df = pd.read_excel("C://Users/mferrera/Documents/Reportes/PIPSA GUATEMALA/MASTER SALES DETAILS PIPSA GT.xlsm", sheet_name="Ventas_PIPGT Analisis (2)", skiprows=2)
    df["Mes"] = df["Fecha"].dt.month_name(locale="es_ES")
    ventas_por_mes = df.groupby("Mes")["TotalVenta"].sum().reset_index().round(2)

    meses_orden = [
        "Octubre", "Noviembre", "Diciembre", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre" 
    ]

    mes_type = CategoricalDtype(categories=meses_orden, ordered=True)
    ventas_por_mes["Mes"] = ventas_por_mes["Mes"].astype(mes_type)
    ventas_por_mes_ordenado = ventas_por_mes.sort_values("Mes").reset_index(drop=True)
    ventas_por_mes_ordenado

    return (ventas_por_mes,)


@app.cell
def _(ventas_por_mes):
    from pandas.api.types import CategoricalDtype

    meses_orden = [
        "Octubre", "Noviembre", "Diciembre", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre" 
    ]

    mes_type = CategoricalDtype(categories=meses_orden, ordered=True)
    ventas_por_mes["Mes"] = ventas_por_mes["Mes"].astype(mes_type)
    ventas_por_mes_ordenado = ventas_por_mes.sort_values("Mes").reset_index(drop=True)
    ventas_por_mes_ordenado
    return


if __name__ == "__main__":
    app.run()
