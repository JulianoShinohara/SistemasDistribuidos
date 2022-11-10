#############################################################################
# Questão 1 - TCP Cliente                                                   #
# Descrição: Envia mensagens para um servidor com uma das seguintes opções: #
#        - CONNECT user, password: Tenta realizar a conexão com servidor    #
#        - PWD: Exibe caminho atual                                         #
#        - CHDIR *path*: Muda o diretório para o *path* especificado        #
#        - GETFILES: Exibe todos os arquivos do diretório atual             #
#        - GETDIRS: Exibe todos os diretórios do diretório atual            #
#        - EXIT: Finaliza a conexão com o servidor                          #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara          #
# Data de criação: 11/09/2022                                               #
# Datas de atualizações: 13/09/2022                                         #
#                        15/09/2022                                         #
#                        18/09/2022                                         #
#                                                                           #
#############################################################################

import socket
import hashlib

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  
clientSocket.connect(addr)

def main():
    authenticator = False  # variável para verificar se está autenticado.
    while True:       
        var = input(">  ")
        varFormated = ''
        
        if(len(var) > 0):
            varFormated = var
            var = (var.split())[0]
          
        match var:
            case 'CONNECT':
                hashPassword = hashlib.sha512(varFormated.split()[2].encode('utf-8')).hexdigest() #hash serve para criptografia da senha
                varFormated = (varFormated.split())[0] + ' ' + (varFormated.split())[1] + ' ' + hashPassword
                clientSocket.send(varFormated.encode('utf-8'))  #envia comando
                connection = clientSocket.recv(1024).decode('utf-8')    #recebe resposta
                
                if(connection == 'SUCCESS'):
                    authenticator = True

                print('Connection: ', connection)   # mostra resposta

            case 'GETFILES':
                if authenticator == True:
                    clientSocket.send(varFormated.encode('utf-8'))
                    listFiles = []
                    quantityFiles = int(clientSocket.recv(1024).decode('utf-8'))
                    print('Found files: ', quantityFiles)

                    if (quantityFiles <= 0):
                        print('There is no file here!')

                    else:
                        files = clientSocket.recv(1024).decode('utf-8') #recebe os arquivos
                        listFiles = files.removeprefix('[').removesuffix("]").split(',') #faz a remoção dos separadores
                        
                        number = 0
                        print(listFiles)
                        for file in listFiles:
                            print(number, '-> ',file.removeprefix(" '").removesuffix("'"))
                            number = number + 1

            case 'GETDIRS':
                if authenticator == True:
                    clientSocket.send(varFormated.encode('utf-8'))
                    listDirFiles = []
                    quantityDirFiles = int(clientSocket.recv(1024).decode('utf-8'))
                    print('Found directories: ', quantityDirFiles) 

                    if quantityDirFiles <= 0:
                        print('There is nothing inside the directory!')

                    else:
                        directory = clientSocket.recv(1024).decode('utf-8')
                        listDirFiles = directory.removeprefix('[').removesuffix(']').split(',')

                        number = 0
                        for file in listDirFiles:
                            print(number, '-> ', file.removeprefix(" '").removesuffix("'"))
                            number = number + 1
                
            case 'EXIT':            
                clientSocket.send(varFormated.encode('utf-8'))
                print(clientSocket.recv(1024).decode('utf-8'))
                clientSocket.close()
                break

            case _:
                clientSocket.send(varFormated.encode('utf-8'))
                print(clientSocket.recv(1024).decode('utf-8'))



if __name__ == "__main__":
    main()