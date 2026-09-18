class FamiliaEdades:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    def calcular_edad_alber(self):
        return (2 * self.edad_juan) / 3

    def calcular_edad_ana(self):
        return (4 * self.edad_juan) / 3

    def calcular_edad_mama(self):
        alber = self.calcular_edad_alber()
        ana = self.calcular_edad_ana()
        return self.edad_juan + alber + ana

    def mostrar_edades(self):
        alber = self.calcular_edad_alber()
        ana = self.calcular_edad_ana()
        mama = self.calcular_edad_mama()

        print("Las edades son:")
        print(f"Alberto: {int(alber)}")
        print(f"Juan: {int(self.edad_juan)}")
        print(f"Ana: {int(ana)}")
        print(f"Mamá: {int(mama)}")


if __name__ == "__main__":
    familia = FamiliaEdades(9)
    familia.mostrar_edades()
