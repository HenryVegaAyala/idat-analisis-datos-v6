import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('ventas_enero_csv.csv')

print(df.head(0)) # Mostrar cabeceras de las columnas

print(df["id_venta"]) # Especifico columna a mostrar

print(df[["id_venta", "producto", "vendedor"]]) # Multiples columnas a mostrar