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
import hashlib
import math
import os
import socket
import threading

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendFile():
    while True:
        print('File name to upload: ')
        fileName = input("> ")        
        file = os.listdir(path='./archiveClient')

        if file.__contains__(fileName):
            if len(fileName) < 256:
                archive = './archiveClient/' + fileName
                fileSize = os.stat(archive).st_size
                qtdFile = math.ceil(fileSize / 1024) # faz a divisão por 1024 para saber em quantas partes o arquivo será enviado 

                with open(archive, "rb") as openFile:
                    checksum = hashlib.sha1(openFile.read()).hexdigest()
                    archiveSend = checksum + ';' + str(qtdFile) + ';' + fileName
                
                    clientSocket.sendto(archiveSend.encode(), addr)
                with open(archive, "rb") as files:
                    bytesFile = files.read(1024)
                    while bytesFile != b'':
                        clientSocket.sendto(bytesFile,addr)
                        bytesFile = files.read(1024)

                print('')
                responseServer, addrServer = clientSocket.recvfrom(1)
                
                if responseServer[0] == 1:
                    print('Download Successfully\n\n')
                   
                else:
                    print('Download Unsuccessfully\n\n')
                    
            else:
                print('File is bigger than 255 bytes\n\n')
               
        else:
            print('Non-existent file\n\n')
            

def main():
    sendThread = threading.Thread(target=sendFile)
    sendThread.start()
                     
if __name__ == "__main__":
    main()
