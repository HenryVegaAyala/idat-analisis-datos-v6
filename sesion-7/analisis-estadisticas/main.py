import pandas as pd

edades = [20, 22, 22, 25, 61]

serie = pd.Series(edades)

media = serie.mean()
mediana = serie.median()
moda = serie.mode()

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda[0]}")