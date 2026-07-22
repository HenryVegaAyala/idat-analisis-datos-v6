import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("datos_clientes.csv")

X = df[["gasto_anual", "visitas_mes"]]

model = KMeans(n_clusters=2)
model.fit(X)

df["cluster"] = model.labels_

print(df)