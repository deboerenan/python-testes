import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

# -------- Fusos horários --------
FUSOS = {
    "Brasil (São Paulo)": "America/Sao_Paulo",
    "Portugal (Lisboa)": "Europe/Lisbon",
    "EUA (Nova York)": "America/New_York",
    "Reino Unido (Londres)": "Europe/London",
    "Japão (Tóquio)": "Asia/Tokyo",
    "Austrália (Sydney)": "Australia/Sydney"
}

# -------- Janela principal --------
root = tk.Tk()
root.title("Relógio com Fuso")
root.geometry("320x200")
root.configure(bg="#0f0f0f")

# -------- Estilo do ComboBox --------
style = ttk.Style()
style.theme_use("default")

style.configure(
    "TCombobox",
    fieldbackground="#1e1e1e",  # fundo do campo
    background="#1e1e1e",       # botão
    foreground="Red"
)

# -------- Variável do país --------
pais_selecionado = tk.StringVar()
pais_selecionado.set("Brasil (São Paulo)")

# -------- ComboBox --------
combo = ttk.Combobox(
    root,
    textvariable=pais_selecionado,
    values=list(FUSOS.keys()),
    state="readonly",
    font=("Arial", 11)
)
combo.pack(pady=15)

# -------- Label do relógio --------
relogio_label = tk.Label(
    root,
    font=("Arial", 28, "bold"),
    fg="red",
    bg="#0f0f0f"
)
relogio_label.pack(pady=10)

# -------- Função do relógio --------
def atualizar_relogio():
    pais = pais_selecionado.get()
    fuso = pytz.timezone(FUSOS[pais])

    hora_atual = datetime.now(fuso).strftime("%H:%M:%S")
    relogio_label.config(text=hora_atual)

    root.after(1000, atualizar_relogio)

atualizar_relogio()
root.mainloop()
