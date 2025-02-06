import tkinter as tk
from tkinter import filedialog, messagebox
from traductor import Traductor # Importamos el traductor

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.root.geometry("600x400")

        self.filename = None    # Guarda el nombre del archivo actual
        self.traductor = Traductor()

        # Menú principal
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menú archivo
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Nuevo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Guardar Como", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.exit_editor)

        self.menu.add_cascade(label="Archivo", menu=file_menu)