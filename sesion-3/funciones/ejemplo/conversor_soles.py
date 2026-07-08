def convertir_a_soles(dolares: float, tipo_de_cambio = 3.8):
    conversion_soles = dolares * tipo_de_cambio
    return conversion_soles

# Caso 1 - Dólares y tipo de cambio por defecto
resultado_caso_1 = convertir_a_soles(100)
print(f"Resultado: {resultado_caso_1}")

# Caso 2 - Dólares y nuevo tipo de cambios
resultado_caso_2 = convertir_a_soles(100, 3.6)
print(f"Resultado: {resultado_caso_2}")