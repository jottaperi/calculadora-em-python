import socket
import tkinter as tk
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 5000

def enviar_dados():
    n1 = entry_num1.get()
    n2 = entry_num2.get()
    operacao = operacao_var.get()

    mensagem = f"{n1};{operacao};{n2}"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((HOST, PORT))
            cliente.send(mensagem.encode())

            resposta = cliente.recv(1024).decode()

            resultado_text.delete("1.0", tk.END)
            resultado_text.insert(tk.END, f"Resultado: {resposta}")

    except ConnectionRefusedError:
        messagebox.showerror(
            "Erro de Conexão",
            "Falha de conexão: O servidor encontra-se indisponível."
        )

janela = tk.Tk()
janela.title("Calculadora Remota")
janela.geometry("400x350")

tk.Label(janela, text="Número 1:").pack()
entry_num1 = tk.Entry(janela)
entry_num1.pack()

tk.Label(janela, text="Operação:").pack()
operacao_var = tk.StringVar()
operacao_var.set("+")
menu_operacao = tk.OptionMenu(janela, operacao_var, "+", "-", "*", "/")
menu_operacao.pack()

tk.Label(janela, text="Número 2:").pack()
entry_num2 = tk.Entry(janela)
entry_num2.pack()

tk.Button(janela, text="Calcular", command=enviar_dados).pack(pady=10)

tk.Label(janela, text="Resultado:").pack()
resultado_text = tk.Text(janela, height=3)
resultado_text.pack()

janela.mainloop()
