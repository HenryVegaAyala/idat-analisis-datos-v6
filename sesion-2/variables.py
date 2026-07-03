# 1. Texto simple -> string
negocio = "Café python!"

# 2. Texto con comilla simple -> string
eslogan = 'El mejor café de la ciudad'

# 3. Número entero -> int
sillas_disponibles = 20

# 4. Número decimal -> float
precio_cafe = 2.50

# 5. Valor booleano -> bool (True)
esta_abierto = True

# 6. Valor booleano -> bool (Falso)
tiene_wifi = False

# 7. Textos largos
direccion = "Av. angamos 635, Miraflores, Lima"

# 8. Número como texto
codigo_postal = "500"

# 9. Variables vacías
proxima_oferta = None

# 10. Variable con caracteres especiales
emoji_cafe = "☕"

# 11. Línea divisoria
print("-" * 60)

# 12. Concatenar variables
concatenar_v1 = negocio + " " + eslogan
print(concatenar_v1)

concatenar_v2 = f"{negocio} {eslogan}"
print(concatenar_v2)

# 13. Concatenación final
print(f"Ejemplo 1-10: Bienvenido {concatenar_v2} {emoji_cafe}")

# 14. Casteo o conversión
print(f"Identificador del tipo de dato {type(codigo_postal)}")

# Convertimos a un valor entero por lo tanto sera un número
numero_codigo_postal = int(codigo_postal)
print(f"Identificador del tipo de dato convertido {type(numero_codigo_postal)}")
print(numero_codigo_postal)

# 15. Ingreso de valores por consola
texto = input("Ingresa un mensaje: ")
print(f"El mensaje es: {texto}")