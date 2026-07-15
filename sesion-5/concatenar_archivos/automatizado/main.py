import pandas as pd
import os
import glob

# Buscar todos los registros en csv automáticamente
buscar_archivos = glob.glob("ventas/ventas_*.csv")

print(f"Cantidad de archivos encontrados: {len(buscar_archivos)}")

dataframes = [] # Variable global

# Leer y concatenar todos los archivos encontrados
for archivo in buscar_archivos:
    df = pd.read_csv(archivo)
    df["ruta"] = archivo
    dataframes.append(df)

consolidado_anual = pd.concat(dataframes, ignore_index=True)

consolidado_anual.to_csv("consolidado/anual_2026.csv", index=False)
consolidado_anual.to_excel("consolidado/anual_2026.xlsx", index=False)