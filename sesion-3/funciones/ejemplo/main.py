def saludo_analista(nombre, apellido):
    saludo = f"Hola {nombre} {apellido}!, estas listo?"
    return saludo

resultado = saludo_analista(apellido="Lozano", nombre="Erik")
print(resultado)

resultado = saludo_analista("Erik", "Lozano")
print(resultado)