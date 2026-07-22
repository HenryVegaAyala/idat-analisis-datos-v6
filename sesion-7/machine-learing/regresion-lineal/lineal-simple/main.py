import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("marketing.csv")

# seleccionar la columna de interés que es la variable independiente (X)
X = df[["marketing"]]

# seleccionar la columna de interés que es la variable dependiente (y)
y = df["ventas"] # Consider que debe ser una seria

# comenzar a entrenar el modelo
model = LinearRegression()
model.fit(X, y) # se encargará de entrenar el modelo con los resultados.

# Creamos el registro de predicción con el nuevo gasto
nueva_fila_marketing = pd.DataFrame([[6000]], columns=["marketing"])
prediccion = model.predict(nueva_fila_marketing)

print(f"La predicción de ventas para una inversión de $6000 en marketing es: {prediccion[0]:.2f}")

# Creamos el registro nuevo de predicción con el nuevo gasto
nueva_fila_marketing = pd.DataFrame([[9000]], columns=["marketing"])
prediccion = model.predict(nueva_fila_marketing)

print(f"La predicción de ventas para una inversión de $9000 en marketing es: {prediccion[0]:.2f}")