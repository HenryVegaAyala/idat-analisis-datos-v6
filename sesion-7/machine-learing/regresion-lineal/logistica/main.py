import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("fuga_clientes.csv")

# seleccionar la columna de interés que es la variable independiente (X)
X = df[["antiguedad", "cuota_mensual"]] # cuando es Logistic se agrega la cantidad de columnas necesarias

# seleccionar la columna de interés que es la variable dependiente (y)
y = df["fuga"] # Consider que debe ser una seria

# comenzar a entrenar el modelo
model = LogisticRegression()
model.fit(X, y) # se encargará de entrenar el modelo con los resultados.

# Creamos el registro de predicción con el nuevo gasto
nueva_fila_fuga = pd.DataFrame([[4, 20]], columns=["antiguedad", "cuota_mensual"])
prediccion = model.predict(nueva_fila_fuga)

if prediccion[0] == 1:
    print("El cliente se va a ir.")
else:
    print("El cliente no se va a ir.")