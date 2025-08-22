import pandas as pd
import xlwings as xw

df = pd.read_csv('2m Sales Records.csv').groupby('Region')['Total Revenue'].sum().reset_index()

xw.Book('datos2.xlsx').sheets['hoja1'].range('A1').value = df
xw.Book('datos2.xlsx').save()
