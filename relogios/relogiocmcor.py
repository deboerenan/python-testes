import tkinter as tk
from datetime import datetime

def atualizar():
    agora = datetime.now().strftime("%H:%M:%S")
    label.config(text=agora)
    root.after(1000, atualizar)

root = tk.Tk()
root.title("Relógio Digital")

# Cor de fundo da janela
root.configure(bg="#000000")


label = tk.Label(
    root,
    font=("Courier", 42, "bold"),
    fg="#00ff00",   # cor do texto
    bg="#000000"    # cor do fundo do label
)

label.pack(padx=20, pady=20)

atualizar()
root.mainloop()
