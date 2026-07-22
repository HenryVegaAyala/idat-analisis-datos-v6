import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("datos_salarios.csv")

# seleccionar la columna de interés que es la variable independiente (X)
X = df[["experiencia", "estudios"]] # cuando es multiple se agrega la cantidad de columnas necesarias

# seleccionar la columna de interés que es la variable dependiente (y)
y = df["salario"] # Consider que debe ser una seria

# comenzar a entrenar el modelo
model = LinearRegression()
model.fit(X, y) # se encargará de entrenar el modelo con los resultados.

# Creamos el registro de predicción con el nuevo gasto
nueva_fila_salario = pd.DataFrame([[4, 5]], columns=["experiencia", "estudios"])
prediccion = model.predict(nueva_fila_salario)

print(f"La predicción de salario para una experiencia de 4 años y 5 estudios es: {prediccion[0]:.2f}")
