import pandas as pd

df = pd.read_csv("mascotas.csv")

moda = df["categoria"].mode()[0]
print(f"Mode: {moda}")

promedio = df["precio"].mean()
print(f"Promedio: {promedio}")