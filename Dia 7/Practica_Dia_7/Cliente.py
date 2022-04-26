import Persona


class Cliente(Persona.Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""-Nombre: {self.nombre} {self.apellido} 
-Numero cuenta: {self.numero_cuenta}
-Saldo: {self.balance}"""

    def ingresar(self,cantidad):
        self.balance += cantidad
        print(f"Se ha ingresado: {cantidad}")
        print(f"Saldo actual en la cuenta: {self.balance}")

    def retirar(self,cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se ha retirado: {cantidad}")
            print(f"Saldo actual en la cuenta: {self.balance}")
        else:
            print(f"Saldo insuficiente, saldo actual en la cuenta: {self.balance}")



