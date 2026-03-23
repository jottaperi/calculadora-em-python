import socket

HOST = '127.0.0.1'
PORT = 5000

def calcular(n1, operacao, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        return "Erro: Entrada inválida"

    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2
    elif operacao == '*':
        return n1 * n2
    elif operacao  == '/':
        if n2 == 0:
            return "Erro: Divisão por zero"
        return n1 / n2
    else:
        return "Operação inválida"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()

    print("Servidor iniciado...")
    print(f"Escutando em {HOST}:{PORT}")

    while True:
        conn, addr = servidor.accept()
        print(f"\nCliente conectado: {addr}")

        with conn:
            dados = conn.recv(1024).decode()

            if not dados:
                continue

            print("Dados recebidos:", dados)

            partes = dados.split(";")
            resultado = calcular(partes[0], partes[1], partes[2])

            print("Resultado enviado:", resultado)

            conn.send(str(resultado).encode())
