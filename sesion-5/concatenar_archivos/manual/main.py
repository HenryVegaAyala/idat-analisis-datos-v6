import pandas as pd

enero = pd.read_csv("ventas_enero.csv")
febrero = pd.read_csv("ventas_febrero.csv")
marzo = pd.read_csv("ventas_marzo.csv")

consolidado = pd.concat([enero, febrero, marzo])

print(consolidado)