import tkinter as tk
from tkinter import messagebox


class ExcepcionesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Excepciones - Ejercicio 6.4")
        self.geometry("420x340")
        self.resizable(False, False)
        
        self.inicializar_componentes()

    def inicializar_componentes(self):
        lbl_titulo = tk.Label(self, text="Seleccione una prueba de excepción:", font=("Arial", 11, "bold"))
        lbl_titulo.pack(pady=15)

        btn_1 = tk.Button(self, text="1. División por Cero (ArithmeticException)", command=self.probar_division_cero, bg="#ffcccc")
        btn_1.pack(fill="x", padx=30, pady=5)

        btn_2 = tk.Button(self, text="2. Objeto Nulo (NullPointerException)", command=self.probar_objeto_nulo, bg="#ffcccc")
        btn_2.pack(fill="x", padx=30, pady=5)

        btn_3 = tk.Button(self, text="3. Índice Fuera de Límites (StringIndexOutOfBounds)", command=self.probar_indice_limite, bg="#ffcccc")
        btn_3.pack(fill="x", padx=30, pady=5)

        btn_4 = tk.Button(self, text="4. Formato de Número Incorrecto (NumberFormatException)", command=self.probar_formato_numero, bg="#ffcccc")
        btn_4.pack(fill="x", padx=30, pady=5)

        btn_original = tk.Button(self, text="Ejecutar Prueba Combinada Original", command=self.probar_ejercicio_original, bg="#d0e1fd")
        btn_original.pack(fill="x", padx=30, pady=15)

    def probar_division_cero(self):
        try:
            print("Ingresando al primer try")
            _ = 10000 / 0
        except ZeroDivisionError:
            print("División por cero")
            messagebox.showerror("Excepción Capturada", "División por cero (ArithmeticException)")
        finally:
            print("Ingresando al primer finally")
            messagebox.showinfo("Bloque Finally", "Ingresando al primer finally")

    def probar_objeto_nulo(self):
        try:
            print("Ingresando al segundo try")
            objeto = None
            _ = objeto.upper() 
        except ZeroDivisionError:
            print("División por cero")
        except Exception as e:
            print("Ocurrió una excepción")
            messagebox.showerror("Excepción Capturada", f"Ocurrió una excepción general: {e}")
        finally:
            print("Ingresando al segundo finally")
            messagebox.showinfo("Bloque Finally", "Ingresando al segundo finally")

    def probar_indice_limite(self):
        try:
            texto = "Programación"
            caracter = texto[14] 
            print(caracter)
        except IndexError:
            print("Indice de string por fuera del límite")
            messagebox.showerror("Excepción Capturada", "Índice de string por fuera del límite (StringIndexOutOfBoundsException)")

    def probar_formato_numero(self):
        try:
            numero = int("Número")
            print(numero)
        except ValueError:
            print("Excepción de formato de número")
            messagebox.showerror("Excepción Capturada", "Excepción de formato de número (NumberFormatException)")
        finally:
            print("Ingresando al finally")
            messagebox.showinfo("Bloque Finally", "Ingresando al finally")

    def probar_ejercicio_original(self):
        resultado_log = []
        
        # Bloque 1
        try:
            resultado_log.append("Ingresando al primer try")
            _ = 10000 / 0
            resultado_log.append("Después de la división")
        except ZeroDivisionError:
            resultado_log.append("División por cero")
        finally:
            resultado_log.append("Ingresando al primer finally")

        # Bloque 2
        try:
            resultado_log.append("Ingresando al segundo try")
            objeto = None
            _ = str(objeto) # Simula comportamiento nulo
            resultado_log.append("Imprimiendo objeto")
        except ZeroDivisionError:
            resultado_log.append("División por cero")
        except Exception:
            resultado_log.append("Ocurrió una excepción")
        finally:
            resultado_log.append("Ingresando al segundo finally")

        mensaje_final = "\n".join(resultado_log)
        print("\n".join(resultado_log))
        messagebox.showinfo("Resultado de Ejecución Combinada", mensaje_final)


if __name__ == "__main__":
    app = ExcepcionesApp()
    app.mainloop()
