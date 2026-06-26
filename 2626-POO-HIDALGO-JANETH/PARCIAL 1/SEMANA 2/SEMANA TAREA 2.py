class CuentaBancaria:
    """Representa una cuenta bancaria simple."""

    def __init__(self, titular, numero, saldo_inicial=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = float(saldo_inicial)

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que 0.")
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= cantidad
        return self.saldo

    def mostrar_detalles(self):
        return (
            f"Titular: {self.titular}\n"
            f"Número de cuenta: {self.numero}\n"
            f"Saldo actual: ${self.saldo:,.2f}"
        )


def main():
    cuenta = CuentaBancaria(titular="Janeth Hidalgo", numero="1234567890", saldo_inicial=500.0)

    print("=== Detalles de la cuenta bancaria ===")
    print(cuenta.mostrar_detalles())

    print("\nDepositando $250.00...")
    cuenta.depositar(250.0)
    print(cuenta.mostrar_detalles())

    print("\nRetirando $100.00...")
    cuenta.retirar(100.0)
    print(cuenta.mostrar_detalles())


if __name__ == "__main__":
    main()
