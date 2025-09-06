import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import xlwings as xw

    df = pd.DataFrame({
                        'vendedor': ['ana', 'luis', 'carlos'],
                        'ventas': [1200, 333, 9000]
    })

    df['comision']=df['ventas']*0.10
    df['total']=df['ventas']+df['comision']
    xw.Book().sheets[0].range('A1').value = df
    return


if __name__ == "__main__":
    app.run()
