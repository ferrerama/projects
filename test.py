import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    df = pd.read_excel("C://Users/mferrera/Documents/Reportes/PIPSA GUATEMALA/MASTER SALES DETAILS PIPSA GT.xlsm", sheet_name="Ventas_PIPGT Analisis (2)", skiprows=2)
    #df["Mes"] = df["Fecha"].dt.month_name(locale="es_ES")
    #ventas_por_mes = df.groupby("Mes")["TotalVenta"].sum().reset_index().round(2)
    #ventas_por_mes
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT
            *
        FROM
        """
    )
    return


if __name__ == "__main__":
    app.run()
