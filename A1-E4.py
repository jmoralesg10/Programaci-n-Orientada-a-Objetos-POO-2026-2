class CalculadoraPotencia:
    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        return self.numero ** 2

    def calcular_cubo(self):
        return self.numero ** 3

    def mostrar_resultados(self):
        cuadrado = self.calcular_cuadrado()
        cubo = self.calcular_cubo()

        print(f"Número ingresado: {self.numero}")
        print(f"El cuadrado es: {cuadrado}")
        print(f"El cubo es: {cubo}")

if __name__ == "__main__":
    calculo = CalculadoraPotencia(4)

    calculo.mostrar_resultados()
