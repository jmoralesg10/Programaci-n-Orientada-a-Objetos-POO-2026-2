import tkinter as tk
from tkinter import messagebox


class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratónProgramación:
    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = [None] * 3  # Máximo 3 integrantes
        self.tamano_equipo = 0

    def esta_lleno(self) -> bool:
        return self.tamano_equipo == len(self.programadores)

    def anadir(self, programador: Programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores[self.tamano_equipo] = programador
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo: str):
        for char in campo:
            if char.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class MaratonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maratón de Programación - Ejercicio 6.7")
        self.geometry("380x380")
        self.resizable(False, False)
        
        self.equipo = None
        self.integrantes_agregados = 0
        self.inicializar_componentes()

    def inicializar_componentes(self):
        # Frame de Datos del Equipo
        self.frame_equipo = tk.LabelFrame(self, text=" 1. Datos del Equipo ", padx=10, pady=10)
        self.frame_equipo.place(x=20, y=20, width=340, height=140)

        tk.Label(self.frame_equipo, text="Equipo:").place(x=10, y=10, width=80, height=20)
        self.campo_nombre_eq = tk.Entry(self.frame_equipo)
        self.campo_nombre_eq.place(x=100, y=10, width=200, height=20)

        tk.Label(self.frame_equipo, text="Universidad:").place(x=10, y=40, width=80, height=20)
        self.campo_univ = tk.Entry(self.frame_equipo)
        self.campo_univ.place(x=100, y=40, width=200, height=20)

        tk.Label(self.frame_equipo, text="Lenguaje:").place(x=10, y=70, width=80, height=20)
        self.campo_lang = tk.Entry(self.frame_equipo)
        self.campo_lang.place(x=100, y=70, width=200, height=20)

        self.btn_crear_equipo = tk.Button(self.frame_equipo, text="Crear Equipo", command=self.crear_equipo, bg="#d0e1fd")
        self.btn_crear_equipo.place(x=100, y=95, width=200, height=22)

        # Frame de Integrantes
        self.frame_integrante = tk.LabelFrame(self, text=" 2. Integrantes del Equipo (Máx. 3) ", padx=10, pady=10)
        self.frame_integrante.place(x=20, y=170, width=340, height=150)

        tk.Label(self.frame_integrante, text="Nombre:").place(x=10, y=10, width=80, height=20)
        self.campo_nom_prog = tk.Entry(self.frame_integrante, state="disabled")
        self.campo_nom_prog.place(x=100, y=10, width=200, height=20)

        tk.Label(self.frame_integrante, text="Apellidos:").place(x=10, y=40, width=80, height=20)
        self.campo_ap_prog = tk.Entry(self.frame_integrante, state="disabled")
        self.campo_ap_prog.place(x=100, y=40, width=200, height=20)

        self.btn_agregar = tk.Button(self.frame_integrante, text="Agregar Integrante (1/3)", command=self.agregar_integrante, bg="#e1fdd0", state="disabled")
        self.btn_agregar.place(x=100, y=75, width=200, height=25)

        self.lbl_estado = tk.Label(self, text="Cree el equipo para comenzar.", fg="gray")
        self.lbl_estado.place(x=20, y=335, width=340, height=20)

    def crear_equipo(self):
        nombre = self.campo_nombre_eq.get().strip()
        univ = self.campo_univ.get().strip()
        lang = self.campo_lang.get().strip()

        if not nombre or not univ or not lang:
            messagebox.showerror("Error", "Todos los campos del equipo son obligatorios.")
            return

        try:
            self.equipo = EquipoMaratónProgramación(nombre, univ, lang)
            messagebox.showinfo("Éxito", f"Equipo '{nombre}' creado correctamente.")
            
            self.campo_nombre_eq.config(state="disabled")
            self.campo_univ.config(state="disabled")
            self.campo_lang.config(state="disabled")
            self.btn_crear_equipo.config(state="disabled")

            self.campo_nom_prog.config(state="normal")
            self.campo_ap_prog.config(state="normal")
            self.btn_agregar.config(state="normal")
            self.lbl_estado.config(text="Agregando integrante 1 de 3", fg="blue")

        except Exception as e:
            messagebox.showerror("Excepción", str(e))

    def agregar_integrante(self):
        if not self.equipo:
            return

        nombre = self.campo_nom_prog.get().strip()
        apellidos = self.campo_ap_prog.get().strip()

        if not nombre or not apellidos:
            messagebox.showerror("Error", "Los campos del integrante no pueden estar vacíos.")
            return

        try:
            EquipoMaratónProgramación.validar_campo(nombre)
            EquipoMaratónProgramación.validar_campo(apellidos)

            prog = Programador(nombre, apellidos)
            self.equipo.anadir(prog)
            self.integrantes_agregados += 1


            self.campo_nom_prog.delete(0, tk.END)
            self.campo_ap_prog.delete(0, tk.END)

            if self.equipo.esta_lleno():
                messagebox.showinfo("Equipo Completo", "Se han registrado los 3 integrantes con éxito.")
                self.campo_nom_prog.config(state="disabled")
                self.campo_ap_prog.config(state="disabled")
                self.btn_agregar.config(state="disabled")
                self.lbl_estado.config(text="Equipo completo registrado satisfactoriamente.", fg="green")
            else:
                self.lbl_estado.config(text=f"Agregando integrante {self.integrantes_agregados + 1} de 3", fg="blue")

        except Exception as e:
            messagebox.showerror("Excepción de Validación", str(e))


if __name__ == "__main__":
    app = MaratonApp()
    app.mainloop()
