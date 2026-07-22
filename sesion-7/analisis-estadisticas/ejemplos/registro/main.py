import pandas as pd

edades = [10, 12, 10, 11, None, 85, 11]

series = pd.Series(edades)

# Calcular la media de las edades, aplicado el filtro
median = series.median()
print(f"Mediana: {median}")

# reemplazar valores Nan
edades_corregidas = series.fillna(median)

resultado = edades_corregidas[edades_corregidas <= 18]

print(f"Resultado: {resultado}")