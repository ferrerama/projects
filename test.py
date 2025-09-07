import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import xlwings as xw
    df = pd.read_csv('download.csv')
    df['comision']=df['Ventas']*0.10
    df['Total']=df['Ventas']+df['comision']
    #xw.Book().sheets[0].range("a1").value = df
    xw.Book().sheets["hoja1"].range("a1").value = df
    #df
    return


if __name__ == "__main__":
    app.run()
