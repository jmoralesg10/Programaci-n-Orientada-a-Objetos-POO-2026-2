import tkinter as tk
from tkinter import messagebox


class Vendedor:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificar_edad(self, edad: int):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        elif 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

    def imprimir(self):
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")


class VendedorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Vendedor - Ejercicio 6.5")
        self.geometry("320x260")
        self.resizable(False, False)
        
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Label(self, text="Nombre:").place(x=20, y=20, width=100, height=20)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=130, y=20, width=160, height=20)

        tk.Label(self, text="Apellidos:").place(x=20, y=60, width=100, height=20)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=130, y=60, width=160, height=20)

        tk.Label(self, text="Edad:").place(x=20, y=100, width=100, height=20)
        self.campo_edad = tk.Entry(self)
        self.campo_edad.place(x=130, y=100, width=160, height=20)

        btn_registrar = tk.Button(self, text="Registrar Vendedor", command=self.registrar_vendedor, bg="#d0e1fd")
        btn_registrar.place(x=20, y=140, width=270, height=30)

        self.lbl_resultado = tk.Label(self, text="", justify="left", fg="#333333")
        self.lbl_resultado.place(x=20, y=180, width=270, height=60)

    def registrar_vendedor(self):
        nombre = self.campo_nombre.get().strip()
        apellidos = self.campo_apellidos.get().strip()
        edad_str = self.campo_edad.get().strip()

        if not nombre or not apellidos or not edad_str:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        try:
            edad = int(edad_str)
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            
            self.lbl_resultado.config(text=vendedor.imprimir(), fg="green")
            messagebox.showinfo("Éxito", "Vendedor registrado correctamente.")
            
        except ValueError as e:
            mensaje_error = str(e) if str(e) else "Error en el formato de la edad."
            self.lbl_resultado.config(text=f"Excepción: {mensaje_error}", fg="red")
            messagebox.showerror("Excepción de Argumento Ilegal", mensaje_error)


if __name__ == "__main__":
    app = VendedorApp()
    app.mainloop()
