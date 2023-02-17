import os
import tkinter as tk
from tkinter import ttk, messagebox

def procesar_archivos():
    root_dir = entry.get()
    old_string = old_string_entry.get()
    new_string = new_string_entry.get()

    # Calcular la cantidad total de archivos a procesar
    total = sum([len(files) for r, d, files in os.walk(root_dir)])
    barra['maximum'] = total

    i = 0
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            # Actualizar la barra de progreso
            i += 1
            barra.step(1)
            root.update_idletasks()

            file_path = os.path.join(subdir, file)
            if file.startswith('index'):
                with open(file_path, 'r') as f:
                    file_content = f.read()
                file_content = file_content.replace(old_string, new_string)
                with open(file_path, 'w') as f:
                    f.write(file_content)

    # Mostrar un mensaje en la ventana de diálogo
    messagebox.showinfo(title="Modificación exitosa", message="Los archivos index han sido modificados exitosamente.")

def cancelar_proceso():
    root.destroy()

root = tk.Tk()
root.title("Ingrese la ruta de la carpeta")
root.geometry("500x300")

label = tk.Label(root, text="Ingrese la ruta de la carpeta:")
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

old_string_label = tk.Label(root, text="Ingrese la cadena a reemplazar:")
old_string_label.pack()
old_string_entry = tk.Entry(root, width=50)
old_string_entry.pack()

new_string_label = tk.Label(root, text="Ingrese la cadena de reemplazo:")
new_string_label.pack()
new_string_entry = tk.Entry(root, width=50)
new_string_entry.pack()

barra = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300)
barra.pack(pady=10)

procesar_button = tk.Button(root, text="Procesar", command=procesar_archivos)
procesar_button.pack(side=tk.LEFT, padx=20, pady=10)

cancelar_button = tk.Button(root, text="Cancelar", command=cancelar_proceso)
cancelar_button.pack(side=tk.RIGHT, padx=20, pady=10)

root.mainloop()
