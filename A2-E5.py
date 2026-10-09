from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2

class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta, interes_mensual=0.0):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta  
        self.saldo = 0.0  
        self.interes_mensual = interes_mensual  

    def imprimir(self):
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.name}")
        print(f"Saldo = {self.saldo}")
        print(f"Interés mensual (%) = {self.interes_mensual * 100}%")

    def consultar_saldo(self):
        print(f"El saldo actual es = {self.saldo}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor:,.1f} en la cuenta. El nuevo saldo es ${self.saldo:,.1f}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor:,.1f} en la cuenta. El nuevo saldo es ${self.saldo:,.1f}")
            return True
        else:
            print("El valor a retirar debe ser mayor que cero y menor o igual al saldo actual.")
            return False

    def calcular_interes_mensual(self):
        interes_ganado = self.saldo * self.interes_mensual
        self.saldo += interes_ganado
        print(f"Se ha aplicado un interés mensual del {self.interes_mensual * 100}%. Ganancia: ${interes_ganado:,.1f}. Nuevo saldo: ${self.saldo:,.1f}")
        return self.saldo


if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS, 0.015)
    
    cuenta.imprimir()
    print()
    
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    
    print("\n--- Aplicando interés mensual ---")
    cuenta.calcular_interes_mensual()
