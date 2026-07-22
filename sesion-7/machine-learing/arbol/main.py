import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dato_credito.csv")

# seleccionar la columna de interés que es la variable independiente (X)
X = df[["ingreso", "morosidad"]] # cuando es Logistic se agrega la cantidad de columnas necesarias

# seleccionar la columna de interés que es la variable dependiente (y)
y = df["aprobado"] # Consider que debe ser una seria

# comenzar a entrenar el modelo
model = DecisionTreeClassifier()
model.fit(X, y) # se encargará de entrenar el modelo con los resultados.

# Creamos el registro de predicción con el nuevo gasto
nueva_fila_fuga = pd.DataFrame([[2800, 0]], columns=["ingreso", "morosidad"])
prediccion = model.predict(nueva_fila_fuga)

if prediccion[0] == 1:
    print("El cliente fue aprobado.")
else:
    print("El cliente no fue aprobado.")