# Calculadora Remota de Expressões 
Este é um projeto de uma calculadora cliente-servidor desenvolvida em Python. A aplicação utiliza a biblioteca socket para permitir que as operações matemáticas sejam processadas de forma remota.

O cliente envia os dados através de uma interface, o servidor realiza o cálculo lógico e devolve o resultado em tempo real.

# Funcionalidades
Interface Gráfica/Interativa: O cliente permite inserir números e escolher a operação.
Processamento Remoto: Toda a lógica matemática é executada no servidor.
Comunicação TCP/IP: Utiliza sockets para garantir a entrega dos dados.
Operações Suportadas: Soma, Subtração, Multiplicação e Divisão.

# Tecnologias Utilizadas
Linguagem: Python 3.x

Biblioteca Principal: socket (comunicação de rede)

Interface: (Se você usou Tkinter ou CustomTkinter, pode citar aqui)

# Estrutura de Arquivos
src/servidor.py: Contém a lógica de processamento e aguarda conexões.
src/cliente.py: Interface que envia os números e a operação escolhida.
src/main.py: Ponto de entrada para execução do sistema.

**Como Executar**
Para rodar o projeto localmente, siga estes passos:
Inicie o Servidor:python src/servidor.py
Inicie o Cliente:python src/cliente.py
