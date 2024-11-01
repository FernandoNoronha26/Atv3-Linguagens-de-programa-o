import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100  # altura em metros
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)
        resultado = f"Seu IMC é: {imc:.2f}"
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para altura e peso.")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x300")
root.configure(bg="#f2f2f2")  # Cor de fundo da janela

# Mensagem de boas-vindas
label_titulo = tk.Label(root, text="Calculadora de IMC", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333")
label_titulo.grid(row=0, column=0, columnspan=3, pady=10)

# Campos de entrada
tk.Label(root, text="Nome:", font=("Arial", 10), bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_nome = tk.Entry(root, font=("Arial", 10), width=30)
entry_nome.grid(row=1, column=1, columnspan=2, pady=5)

tk.Label(root, text="Endereço:", font=("Arial", 10), bg="#f2f2f2").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_endereco = tk.Entry(root, font=("Arial", 10), width=30)
entry_endereco.grid(row=2, column=1, columnspan=2, pady=5)

tk.Label(root, text="Altura (cm):", font=("Arial", 10), bg="#f2f2f2").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_altura = tk.Entry(root, font=("Arial", 10), width=10)
entry_altura.grid(row=3, column=1, pady=5)

tk.Label(root, text="Peso (kg):", font=("Arial", 10), bg="#f2f2f2").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_peso = tk.Entry(root, font=("Arial", 10), width=10)
entry_peso.grid(row=4, column=1, pady=5)

# Botões
btn_calcular = tk.Button(root, text="Calcular IMC", font=("Arial", 10), command=calcular_imc, bg="#4CAF50", fg="white", width=10)
btn_calcular.grid(row=5, column=0, pady=20, padx=5)

btn_reiniciar = tk.Button(root, text="Reiniciar", font=("Arial", 10), command=reiniciar, bg="#2196F3", fg="white", width=10)
btn_reiniciar.grid(row=5, column=1, pady=20, padx=5)

btn_sair = tk.Button(root, text="Sair", font=("Arial", 10), command=root.quit, bg="#f44336", fg="white", width=10)
btn_sair.grid(row=5, column=2, pady=20, padx=5)

# Resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f2f2f2", fg="#333")
label_resultado.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
