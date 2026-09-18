class Empleado:
    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (self.porcentaje_retencion / 100)

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion = self.calcular_retencion()
        return salario_bruto - retencion

    def mostrar_resultados(self):
        bruto = self.calcular_salario_bruto()
        retencion = self.calcular_retencion()
        neto = self.calcular_salario_neto()

        print("--- Liquidación de nómina ---")
        print(f"Horas trabajadas: {self.horas_trabajadas}")
        print(f"Valor por hora: ${self.valor_hora:,.0f}")
        print(f"Salario Bruto: ${bruto:,.2f}")
        print(f"Retención en la fuente (12.5%): ${retencion:,.2f}")
        print(f"Salario Neto: ${neto:,.2f}")

if __name__ == "__main__":
    empleado1 = Empleado(horas_trabajadas=48, valor_hora=5000, porcentaje_retencion=12.5)

    empleado1.mostrar_resultados()
