#################################################################################################################### 
# Questão 2 - UDP CLIENT                                                                                           #                                                                              #
# Descrição: Fazer um sistema de upload de arquivos via UDP. Um servidor UDP deverá receber as partes dos arquivos #
#(1024 bytes), verificar ao final a integridade via um checksum (SHA-1) e armazenar o arquivo em uma pasta padrão. #
#Sugestões: o servidor pode receber o nome e tamanho do arquivo como o primeiro pacote e o checksum como o último. #
#Testar o servidor com arquivos textos e binários (ex: imagens, pdf) de tamanhos arbitrários (ex: 100 bytes, 4KiB, #
#4MiB). O protocolo para a comunicação deve ser criado e especificado textualmente ou graficamente.                #
#                                                                                                                  #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                                                 #
# Data de criação: 23/09/2022                                                                                      #
# Data de modificação: 25/09/2022                                                                                  #  
#                      26/09/2022                                                                                  #    
####################################################################################################################
import socket
import os
import math
import hashlib

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
                fileSize = int.to_bytes((os.stat('./archiveClient/' + fileName).st_size), 4, 'big')
                qtdFile = math.ceil(aux / 1024) # faz a divisão por 1024 para saber em quantas partes o arquivo será enviado 
                clientSocket.send(fileSize)
                openFile = open('./archiveClient/' + fileName,'rb')  # leitura binário

                # faz o checksum (soma de verificação) no arquivo para verifica-lo
                checksum = openFile.read()
                sha1_hash = hashlib.sha1(checksum)               
                checksum = sha1_hash.hexdigest() # hexdigest retorna como um objeto string de comprimento duplo, contendo apenas dígitos hexadecimais
               # checksum = hashlib.sha1(openFile.read()).hexdigest() # faz o checksum (soma de verificação) no arquivo para verifica-lo
                
                # file = fileName + str(fileSize) + checksum + str(qtdFile)
                # print('file: ', file)
                # clientSocket.sendto(file.encode(), addr)

                openFile.seek(0) # seek é usado para que abra o arquivo para ler desde o inicio, já que tivemos que dividir o arquivo em pedaços
                
                for _ in range(qtdFile):
                    clientSocket.sendto(openFile.read(1024), addr) #envia para o servidor
                    print('addr: ', addr)

                print('checksum: ', checksum)
                clientSocket.sendto(checksum.encode(), addr)
                openFile.close() 

            else: print('ERROR!')
        
        else: print('There is no file here with this name!')
                
                     
if __name__ == "__main__":
    main()