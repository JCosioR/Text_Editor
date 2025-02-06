import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.root.geometry("600x400")

        self.filename = None    # Guarda el nombre del archivo actual

        # Menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Nuevo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_command(label="Guardar Como", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.exit_editor)

        self.menu.add_cascade(label="Archivo", menu=file_menu)

        #### Se debe modificar el código para incluir un nuevo menú llamado "Proyecto" ###
        

        # Área de texto
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=1, fill="both")

    def update_title(self, name="Editor de Texto"):
        self.root.title(name)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.update_title("Nuevo Archivo - Editor de Texto")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt"), ("Todos", "*.*")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            self.filename = file_path
            self.update_title(f"{file_path} - Editor de Texto")

    def save_file(self):
        if self.filename:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as()
    
    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"), ("Todos", "*.*")])
        if file_path:
            self.filename = file_path
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.update_title(f"{file_path} - Editor de Texto")
    
    def exit_editor(self):
        if messagebox.askyesno("Salir", "¿Deseas salir del editor?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()