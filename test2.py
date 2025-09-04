import pandas as pd

def bono(ventas):
    if ventas > 1000:
        return ventas * 0.1
    else:
        return 0

df = pd.DataFrame({
    'Vendedor': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Ventas': [1200, 800, 1500, 700]
})

df['Bono'] = df['Ventas'].apply(bono)
df['Total'] = df['Ventas'] + df['Bono']
df.to_csv('calculo_bono.csv', index=False)
print(df)