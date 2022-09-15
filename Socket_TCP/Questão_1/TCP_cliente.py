'''
# Questão 1 - TCP Cliente 
# Descrição: Envia mensagens para um servidor com uma das seguintes opções:
        - CONNECT user, password: Tenta realizar a conexão com servidor
        - PWD: Exibe caminho atual
        - CHDIR *path*: Muda o diretório para o *path* especificado 
        - GETFILES: Exibe todos os arquivos do diretório atual
        - GETDIRS: Exibe todos os diretórios do diretório atual
        - EXIT: Finaliza a conexão com o servidor
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara
# Data de criação: 11/09/2022
# Datas de atualizações: 13/09/2022
                         15/09/2022

'''

import socket

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.connect(addr)
serverSocket.sendall(str.encode('teste teste'))
data = serverSocket.recv(1024)
print('Mensagem: ',data.decode())

connect = False
while True:
    var = input()
    match var:
        case 'CONNECT':
            print('')

        case 'PWD':
            print('')

        case 'CHDIR':
            print('')

        case 'GETFILES':
            print('')

        case 'GETDIRS':
            print('') 

        case 'EXIT':
            data = serverSocket.recv(1024)
            print('Mensagem: ',data.decode())
            serverSocket.close()