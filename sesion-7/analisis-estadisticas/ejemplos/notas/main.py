import pandas as pd

df = pd.read_csv("notas.csv")

media = df["notas"].mean()
mediana = df["notas"].median()

print(f"Media: {media}") # Promedio
print(f"Mediana: {mediana}")