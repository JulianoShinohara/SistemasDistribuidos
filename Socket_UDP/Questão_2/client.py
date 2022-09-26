################################################################################################################# 
# Questão 2 - UDP CLIENT                                                                                        #                                                                              #
# Descrição: 
# 
#   
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                                              #
# Data de criação: 23/09/2022                                                                                   #
# Data de modificação: 25/09/2022 
#################################################################################################################
import socket
import os
import math
import hashlib

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  
clientSocket.connect(addr)

def main():
    while True:
        print('Nome do arquivo para upload: \n')
        fileName = input(">  ")        
        file = os.listdir(path='./archiveClient')
        aux = len(fileName)

        if(file.__contains__(fileName)):
            if (aux < 256):
                fileSize = int.to_bytes((os.stat('./files' + fileName).st_size), 4, 'big')
                qtdFile = math.ceil(aux / 1024) # faz a divisão por 1024 para saber em quantas partes o arquivo será enviado 
                clientSocket.send(fileSize)
                openFile = open('./files/' + fileName,'rb')  # leitura binário
                # faz o checksum (soma de verificação) no arquivo para verifica-lo
                checksum = openFile.read()
                md5_hash = hashlib.md5()
                md5_hash.update(checksum)
                checksum = md5_hash.hexdigest()
               # checksum = hashlib.sha1(openFile.read()).hexdigest() # faz o checksum (soma de verificação) no arquivo para verifica-lo
                
                file = fileName + str(fileSize) + checksum + str(qtdFile)
                clientSocket.sendto(file.encode(), addr)

                openFile.seek(0) # seek é usado para que abra o arquivo para ler desde o inicio, já que tivemos que dividir o arquivo em pedaços
                
                while openFile.read(1024) != b'':
                    clientSocket.sendto(openFile.read(1024), addr) #envia para o servidor
                    openFile.close() 

                clientSocket.sendto(checksum.encode(), addr)
            
            else: print('ERROR!')
        
        else: print('There is no file here with this name!')
                
        clientSocket.send(fileName) 

               
if __name__ == "__main__":
    main()