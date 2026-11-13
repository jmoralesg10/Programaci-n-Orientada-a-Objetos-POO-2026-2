import math
import tkinter as tk
from tkinter import messagebox


class CálculosNuméricos:
    
    @staticmethod
    def calcular_logaritmo_neperiano(valor: float) -> float:
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo para calcular el logaritmo.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> float:
        if valor < 0:
            raise ValueError("El valor debe ser un número positivo para calcular la raíz cuadrada.")
        return math.sqrt(valor)


class CalculosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculos Numéricos - Ejercicio 6.6")
        self.geometry("360x260")
        self.resizable(False, False)
        
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Label(self, text="Valor numérico:").place(x=20, y=20, width=100, height=25)
        self.campo_valor = tk.Entry(self)
        self.campo_valor.place(x=130, y=20, width=200, height=25)

        btn_calcular = tk.Button(self, text="Calcular", command=self.ejecutar_calculos, bg="#d0e1fd")
        btn_calcular.place(x=20, y=60, width=310, height=30)

        self.lbl_resultado = tk.Label(self, text="", justify="left", fg="#333333")
        self.lbl_resultado.place(x=20, y=110, width=310, height=130)

    def ejecutar_calculos(self):
        valor_str = self.campo_valor.get().strip()
        resultados = []

        try:
            if not valor_str:
                raise ValueError("El campo no puede estar vacío.")
            
            valor = float(valor_str.replace(',', '.'))
            
            try:
                log_val = CálculosNuméricos.calcular_logaritmo_neperiano(valor)
                resultados.append(f"Resultado Logaritmo: {log_val:.4f}")
            except ValueError as e:
                resultados.append(f"Logaritmo: {e}")

            try:
                sqrt_val = CálculosNuméricos.calcular_raiz_cuadrada(valor)
                resultados.append(f"Resultado Raíz: {sqrt_val:.4f}")
            except ValueError as e:
                resultados.append(f"Raíz: {e}")

            self.lbl_resultado.config(text="\n".join(resultados), fg="blue")

        except ValueError as e:
            error_msg = f"Error de entrada: {e}" if "could not convert" not in str(e) else "El valor debe ser numérico (InputMismatch)."
            self.lbl_resultado.config(text=error_msg, fg="red")
            messagebox.showerror("Excepción Capturada", error_msg)


if __name__ == "__main__":
    app = CalculosApp()
    app.mainloop()
