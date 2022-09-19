############################################################################
# Questão 1 - TCP Servidor                                                 #
# Descrição: Envia mensagens para o cliente utilizando uma das opções:     #
#        - CONNECT user, password: Tenta estabelecer a conexão com cliente #
#        - PWD: Exibe diretório atual                                      #
#        - CHDIR *path*: Altera o diretório para o *path* especifica       #
#        - GETFILES: Exibe todos os arquivos do diretório atual            #
#        - GETDIRS: Exibe todos os diretórios atuais                       #
#        - EXIT: Finaliza a conexão com o cliente                          #
#                                                                          #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara         #
# Data de criação: 11/09/2022                                              #
# Datas de atualizações: 13/09/2022                                        #
#                        15/09/2022                                        #
#                        18/09/2022                                        #
############################################################################

from asyncio.log import logger
from genericpath import isfile
import logging
from multiprocessing import connection
from operator import truediv
import os
import socket
import threading

HOST = ""
PORT = 6000
addr = (HOST, PORT)
user = 'Gaby'
password = 'd404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db'

#Cria socket e define a instancia
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)
#Define o formato do log
formatLog = '%(asctime)-1s %(userIP)s %(userPort)s %(message)s'
logging.basicConfig(format=formatLog, level=20)
nameLog = logging.getLogger('TCP_Server')

def connectionClient(ip, port, connection):
    # variável para verificar se user está autenticado.
    authenticator = False
    dados = {'userIP': ip, 'userPort': port}
    while True:

        # Cria variavel que recebe e descriptografa a mensagem.
        messageReceive = ''
        messageReceive = connection.recv(1024).decode()

        if len(messageReceive.split()) > 1:
            connect = messageReceive
            messageReceive = (messageReceive.split())[0]
        match messageReceive:
            case 'CONNECT':
                userClient = (connect.split())[1]
                userPassword = (connect.split())[2]
                nameLog.info('Protocol: %s', 'received CONNECT request', extra = dados)            
                # Verifica se usuário é valido
                if userClient == user:
                    # Verifica se a senha está correta
                    if userPassword == password:
                        nameLog.info('Protocol: %s', 'successfully connected', extra = dados)
                        connection.send(('SUCCESS').encode('utf-8'))
                        authenticator = True
                    else:
                        nameLog.info('Protocol: %s', 'invalid connection', extra = dados)            
                        connection.send(('ERROR').encode('utf-8'))
                else:
                    nameLog.info('Protocol: %s', 'invalid connection', extra = dados)            
                    connection.send(('ERROR').encode('utf-8'))
            

            case 'PWD':
                if authenticator == True:
                    nameLog.info('Protocol: %s', 'received PWD request', extra = dados)            
                    directory: os.PathLike = os.getcwd()
                    connection.send((directory).encode('utf-8'))
                else:
                    nameLog.info('Protocol: %s', 'need CONNECTION', extra = dados)            
                    connection.send(('ERROR').encode('utf-8'))

            case 'CHDIR':
                if authenticator == True:
                    nameLog.info('Protocol: %s', 'received CHDIR request', extra = dados)            
                    if len(connect.split()) > 1 and os.path.isdir((connect.split())[1]):
                        os.chdir((connect.split())[1])
                        connection.send('SUCCESS'.encode('utf-8'))
                        nameLog.info('Protocol: %s', ' successfully CHDIR', extra=dados)
                    else:
                        nameLog.info('Protocol: %s', 'invalid connection', extra = dados)            
                        connection.send(('ERROR').encode('utf-8'))
                else:
                    nameLog.info('Protocol: %s', 'need CONNECTION', extra = dados)            
                    connection.send(('ERROR').encode('utf-8'))
 
            case 'GETFILES':
                if authenticator == True:
                    nameLog.info('Protocol: %s', 'received GET FILES request', extra = dados)            
                    # Quantidade de arquivos
                    quantityFiles = 0
                    # Nome dos arquivos
                    listFiles: list[str] = []

                    # Diretório utilizado
                    directory = str(os.getcwd())
                    # Dados armazenados no diretório
                    files = os.listdir(directory)

                    for name in files:
                        if os.path.isfile(str(directory + '\\' + name)):
                            quantityFiles = quantityFiles + 1
                            listFiles.append(str(name))
                    
                    if quantityFiles > 0:
                        # Envia o número de arquivos para o cliente
                        connection.send(str(quantityFiles).encode('utf-8'))
                        # Envia a lista com o nome dos arquivos para o cliente
                        connection.send(str(listFiles).encode('utf-8'))
                    else:
                        connection.send(('0').encode())

                    nameLog.info('Protocol: %s', ' successfully GETFILES', extra=dados)
                else:
                    nameLog.info('Protocol: %s', 'need CONNECTION', extra = dados)            
                    connection.send(('ERROR').encode('utf-8'))
            
            case 'GETDIRS':
                if authenticator == True:
                    nameLog.info('Protocol: %s', 'received GET DIRS request', extra = dados)            
                    # Quantidade de arquivos
                    quantityFiles = 0
                    # Nome dos arquivos
                    listDirFiles: list[str] = []
                    # Diretório utilizado
                    directory = str(os.getcwd())
                    # Dados armazenados no diretório
                    files = os.listdir(directory)

                    for name in files:
                        if os.path.isfile(str(directory + '\\' + name)):
                            quantityFiles = quantityFiles + 1
                            listDirFiles.append(str(name))

                    if quantityFiles > 0:
                        # Envia o número de arquivos para o cliente
                        connection.send(str(quantityFiles).encode('utf-8'))
                        # Envia a lista com o nome dos arquivos para o cliente
                        connection.send(str(listDirFiles).encode('utf-8'))
                    else:
                        connection.send(('0').encode())
                    nameLog.info('Protocol: %s', ' successfully GETFILES', extra=dados)
                else:
                    nameLog.info('Protocol: %s', 'need CONNECTION', extra = dados)            
                    connection.send(('ERROR').encode())

            case 'EXIT':
                if authenticator == True:
                    nameLog.info('Protocol: %s', 'received EXIT request', extra = dados)            
                    connection.send(('Finish connection').encode())
                    connection.close()
                    authenticator = False
                    break

def main():
    threads = []

    while True:
        serverSocket.listen(3)
        (connection, (ip, port)) = serverSocket.accept()
        dados = {'userIP': ip, 'userPort': port}
        nameLog.info('Protocol: %s', 'succesfully connection', extra = dados)            
        
        thread = threading.Thread( target=connectionClient, args=(ip, port, connection))
        thread.start()

        threads.append(thread)

        for sockets in threads:
            sockets.join()

        serverSocket.close()
        



if __name__ == "__main__":
    main()