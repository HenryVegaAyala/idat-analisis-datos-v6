# 1. Crear una lista de productos: Ejemplo de una lista de cadenas
vitrina = ["Pan", "Alfajor", "Aceite", "Mantequilla"]
print(vitrina)

# 2. Ejemplo de una lista de números
ventas_hora = [10, 20, 15, 30]

# 3. Ejemplo de valores mixtos
valores_mixtos = [10, 20.50, "Hola", True, False]

# 4. Acceder a un elemento de una lista basada en índice
primer_elemento = vitrina[0]
print(f"Primer producto: {primer_elemento}")

# 5. Acceder al último elemento de una lista
ultimo_elemento = vitrina[-1]
print(f"Último producto: {ultimo_elemento}")

# 6. Agregar un nuevo producto a la lista
vitrina.append("Donut")
print(f"Lista de productos agregados: {vitrina}")

# 7. Cambiar o actualizar producto de la lista
vitrina[2] = "Aceite de oliva"
print(f"Lista de productos actualizada: {vitrina}")

# 8. Eliminar un producto de la lista
vitrina.remove("Pan")
print(f"Lista de productos eliminados: {vitrina}")

# 9. Eliminar un producto basado en el índice de una lista
del vitrina[1]
print(f"Lista de productos eliminados: {vitrina}")

# 10. Obtener la cantidad registros de una lista
total = len(vitrina)
print(f"Total de productos en la vitrina: {total}")