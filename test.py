import pandas as pd

df = pd.read_csv('2m Sales Records.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
print(df.head(3))

