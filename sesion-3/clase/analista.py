class Analista:
    def __init__(self, nombre: str, nivel: str):
        self.nombre = nombre
        self.nivel = nivel

    def saludo(self):
        mensaje = f"Hola {self.nombre}, tu impuesto: {self.nivel}"
        print(mensaje)

analista_1 = Analista("Erik Lozano", "Senior")
analista_1.saludo()
analista_1.saludo()
analista_1.saludo()
