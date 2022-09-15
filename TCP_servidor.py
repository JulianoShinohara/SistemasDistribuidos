'''
# Questão 1 - TCP Servidor 
# Descrição: Envia mensagens para um cliente com uma das seguintes opções:
        - CONNECT user, password: Tenta realizar a conexão com cliente
        - PWD: Exibe caminho atual
        - CHDIR *path*: Muda o diretório para o *path* especificado 
        - GETFILES: Exibe todos os arquivos do diretório atual
        - GETDIRS: Exibe todos os diretórios do diretório atual
        - EXIT: Finaliza a conexão com o cliente
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara
# Data de criação: 11/09/2022
# Datas de atualizações: 13/09/2022
                         15/09/2022

'''

import socket

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)
user = 'Gaby'
password = 'teste1teste2teste3'


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.bind(addr)
serverSocket.listen()
print('Waiting Connection')
connection, address = serverSocket.accept()

print("Connect in address", address)

while True:
    data = connection.recv(1024)
    if not data:
        print("Close connection")
        connection.close()
        break
    connection.sendall(data)
    print(data)