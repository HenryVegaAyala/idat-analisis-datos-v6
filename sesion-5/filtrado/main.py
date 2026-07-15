import pandas as pd

# Lectura del archivo .txt
df = pd.read_csv("dataset.txt")

print(df.info())

filtro_por_unidades_vendidas = df["Units Sold"] > 20

resultado = df[filtro_por_unidades_vendidas]

print(resultado.info())