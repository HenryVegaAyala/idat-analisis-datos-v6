import pandas as pd

datos = {
    "nombre": ["Luis", "Miguel", "Juan"],
    "edad": [25, 30, 35],
    "genero": ["Masculino", "Masculino", "Masculino"],
}

resultado = pd.DataFrame(datos)

print(resultado)