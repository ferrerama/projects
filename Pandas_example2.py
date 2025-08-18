import pandas as pd

df = pd.read_csv("2m Sales Records.csv")

ventasxpais = df.groupby('Country')['Total Revenue'].sum()
print (ventasxpais)