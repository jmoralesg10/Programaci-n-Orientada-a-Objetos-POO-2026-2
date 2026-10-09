from enum import Enum

class TipoCom(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODISESEL = 4
    GAS_NATURAL = 5

class TipoA(Enum):
    CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6

class TipoColor(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, numero_puertas, cantidad_asientos, velocidad_maxima, color, es_automatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.es_automatico = es_automatico
        self.velocidad_actual = 0  
        self.cantidad_multas = 0 
        self.valor_multa_unitaria = 150000  

    def get_marca(self): return self.marca
    def set_marca(self, marca): self.marca = marca

    def get_modelo(self): return self.modelo
    def set_modelo(self, modelo): self.modelo = modelo

    def get_motor(self): return self.motor
    def set_motor(self, motor): self.motor = motor

    def get_tipo_combustible(self): return self.tipo_combustible
    def set_tipo_combustible(self, tipo_combustible): self.tipo_combustible = tipo_combustible

    def get_tipo_automovil(self): return self.tipo_automovil
    def set_tipo_automovil(self, tipo_automovil): self.tipo_automovil = tipo_automovil

    def get_numero_puertas(self): return self.numero_puertas
    def set_numero_puertas(self, numero_puertas): self.numero_puertas = numero_puertas

    def get_cantidad_asientos(self): return self.cantidad_asientos
    def set_cantidad_asientos(self, cantidad_asientos): self.cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self): return self.velocidad_maxima
    def set_velocidad_maxima(self, velocidad_maxima): self.velocidad_maxima = velocidad_maxima

    def get_color(self): return self.color
    def set_color(self, color): self.color = color

    def get_velocidad_actual(self): return self.velocidad_actual
    def set_velocidad_actual(self, velocidad_actual): self.velocidad_actual = velocidad_actual

    def get_es_automatico(self):
        return self.es_automatico

    def set_es_automatico(self, es_automatico):
        self.es_automatico = es_automatico

    def acelerar(self, incremento_velocidad):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual += incremento_velocidad
        else:
            print("¡Alerta! Se intentó superar la velocidad máxima permitida.")
            print("Se ha generado una multa por exceso de velocidad.")
            self.velocidad_actual = self.velocidad_maxima
            self.cantidad_multas += 1

    def desacelerar(self, decremento_velocidad):
        if self.velocidad_actual - decremento_velocidad >= 0:
            self.velocidad_actual -= decremento_velocidad
        else:
            print("No se puede desacelerar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def tiene_multas(self):
        return self.cantidad_multas > 0

    def calcular_valor_total_multas(self):
        return self.cantidad_multas * self.valor_multa_unitaria

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            return 0
        return distancia / self.velocidad_actual

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible.name}")
        print(f"Tipo de automóvil = {self.tipo_automovil.name}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Color = {self.color.name}")
        print(f"Es automático = {self.es_automatico}")
        print(f"Velocidad actual = {self.velocidad_actual}")


if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 5, 6, 250, TipoColor.NEGRO, True)
    
    print("--- Estado inicial ---")
    auto1.imprimir()
    
    print("\n--- Ejecutando pruebas de velocidad y multas ---")
    auto1.set_velocidad_actual(100)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    
    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    
    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")
    
    auto1.frenar()
    print(f"Velocidad actual = {auto1.get_velocidad_actual()}")

    print("\n--- Intentando superar la velocidad máxima ---")
    auto1.set_velocidad_actual(240)
    auto1.acelerar(30)  
    print(f"Velocidad actual limitada a = {auto1.get_velocidad_actual()}")
    print(f"¿Tiene multas?: {auto1.tiene_multas()}")
    print(f"Valor total de multas: ${auto1.calcular_valor_total_multas():,.0f}")
