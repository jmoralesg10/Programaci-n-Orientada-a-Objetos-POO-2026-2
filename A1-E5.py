import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_longitud(self):
        return 2 * math.pi * self.radio

    def mostrar_resultados(self):
        area = self.calcular_area()
        longitud = self.calcular_longitud()

        print(f"Radio ingresado: {self.radio}")
        print(f"El área del círculo es: {area:.2f}")
        print(f"La longitud de la circunferencia es: {longitud:.2f}")

if __name__ == "__main__":
    mi_circulo = Circulo(5)
  
    mi_circulo.mostrar_resultados()
