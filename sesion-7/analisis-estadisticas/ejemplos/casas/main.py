import pandas as pd

df = pd.read_csv("casas.csv")

cantidad_nullos = df["precios"].isnull().sum()

print(f"Cantidad de nullos: {cantidad_nullos}")

describe = df.describe()

print(describe)