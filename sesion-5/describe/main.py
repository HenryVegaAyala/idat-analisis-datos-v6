import pandas as pd

descripcion = pd.read_csv("ventas_enero_csv.csv")

print(descripcion.describe())