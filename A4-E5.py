import tkinter as tk
from tkinter import messagebox, filedialog


class LeerArchivo:
    @staticmethod
    def leer_contenido(ruta_archivo: str, convertir_mayusculas: bool = False) -> str:
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                if convertir_mayusculas:
                    contenido = contenido.upper()
                return contenido
        except FileNotFoundError:
            raise FileNotFoundError("No se pudo encontrar el archivo especificado.")
        except Exception as e:
            raise IOError(f"Error al leer el archivo: {e}")


class LectorArchivoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lectura de Archivos - Ejercicio 6.8")
        self.geometry("420x380")
        self.resizable(False, False)
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Label(self, text="Archivo de texto:").place(x=20, y=20, width=120, height=20)
        self.campo_ruta = tk.Entry(self)
        self.campo_ruta.insert(0, "prueba.txt")
        self.campo_ruta.place(x=140, y=20, width=210, height=20)

        btn_examinar = tk.Button(self, text="...", command=self.examinar_archivo)
        btn_examinar.place(x=360, y=20, width=30, height=20)

        self.var_mayusculas = tk.BooleanVar()
        self.chk_mayusculas = tk.Checkbutton(self, text="Convertir caracteres a mayúsculas", variable=self.var_mayusculas)
        self.chk_mayusculas.place(x=140, y=50, width=250, height=20)

        btn_leer = tk.Button(self, text="Leer y Mostrar Contenido", command=self.ejecutar_lectura, bg="#d0e1fd")
        btn_leer.place(x=20, y=80, width=370, height=30)

        self.area_texto = tk.Text(self, wrap="word")
        self.area_texto.place(x=20, y=130, width=370, height=220)

    def examinar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            self.campo_ruta.delete(0, tk.END)
            self.campo_ruta.insert(0, ruta)

    def ejecutar_lectura(self):
        ruta = self.campo_ruta.get().strip()
        mayusculas = self.var_mayusculas.get()

        if not ruta:
            messagebox.showerror("Error", "Debe ingresar el nombre o la ruta del archivo.")
            return

        try:
            contenido = LeerArchivo.leer_contenido(ruta, mayusculas)
            self.area_texto.delete("1.0", tk.END)
            self.area_texto.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Excepción de E/S", str(e))
            self.area_texto.delete("1.0", tk.END)
            self.area_texto.insert(tk.END, "No se pudo leer el archivo.")


if __name__ == "__main__":
    app = LectorArchivoApp()
    app.mainloop()
