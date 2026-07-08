class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            print(f"Compra realizada con éxito. saldo restante: {self.saldo}")
        else:
            print(f"Fondos insuficientes. saldo actual: {self.saldo}")


cliente_1 = Cliente("Luis", 1000)
cliente_1.comprar(500) # compro un celular y el saldo a mostrar seria 500
cliente_1.comprar(200) # compro unos audífonos y el saldo a mostrar sería 300
cliente_1.comprar(500) # compro un reloj y el saldo a mostrar sería 300, ya que no tiene fondos suficientes para realizar la compra