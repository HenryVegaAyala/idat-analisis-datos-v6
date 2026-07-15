import os
import pandas as pd

print(os.getcwd()) # Ayuda a identificar el directorio de trabajo actual

archivos = os.listdir(".")
print(archivos) # Muestra los archivos y carpetas en el directorio actual

# Validaciones de archivos con rutas absolutas
ruta_archivo = f"{os.getcwd()}/ventas_enero_csv.csv"

if os.path.exists(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    print("Se encontro el archivo y se cargó en un DataFrame")
else:
    print(f"No encontré el archivo {ruta_archivo}")