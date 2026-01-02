import tkinter as tk
from datetime import datetime

def atualizar():
    agora = datetime.now().strftime("%H:%M:%S")
    label.config(text=agora)
    root.after(1000, atualizar)

root = tk.Tk()
root.title("Relógio")

label = tk.Label(root, font=("Arial", 40))
label.pack(padx=20, pady=20)

atualizar()
root.mainloop()
