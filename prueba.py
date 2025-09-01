import pandas as pd
df = pd.read_csv('prueba.csv')
df['comision'] = df['Ventas'] * 0.10
df['total'] = df['Ventas'] + df['comision']
df.to_csv('prueba2.csv', index=False)
print(df)
