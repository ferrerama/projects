import pandas as pd
import xlwings as xw

ventas = pd.DataFrame([100, 200, 1000])
comision = ventas * 0.05
total = ventas + comision
print(total)