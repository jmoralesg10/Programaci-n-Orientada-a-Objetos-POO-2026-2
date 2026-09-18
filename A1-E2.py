class OperacionMatematica:
    def __init__(self):
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar_instrucciones(self):
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y

    def mostrar_resultado(self):
        print(f"El valor de la suma es: {self.suma}")

if __name__ == "__main__":
    proceso = OperacionMatematica()

    proceso.ejecutar_instrucciones()
    proceso.mostrar_resultado()
