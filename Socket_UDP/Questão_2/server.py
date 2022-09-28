#################################################################################################################### 
# Questão 2 - UDP SERVIDOR                                                                                           #                                                                              #
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
import logging
import hashlib

HOST = "127.0.0.1"
PORT = 6000
addr = (HOST, PORT)

# Cria socket e define a instancia
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)

# Define o formato do log
formatLog = '%(asctime)-1s %(userIP)s %(userPort)s %(message)s'
logging.basicConfig(format=formatLog, level=20)
nameLog = logging.getLogger('UDPServer')

def main():
    while True:
        archive = b''

        requestClient, addr = serverSocket.recvfrom(1024)
        messageClient = requestClient.decode().split(';')
        dados = {'userIP': addr[0], 'userPort': addr[1]}

        checksumClient = messageClient[0]
        qtyPackets = messageClient[1]
        fileName = messageClient[2]
        archiveDirectory = './archiveServer/' + str(fileName)
        
        nameLog.info('Protocol: %s', 'Downloading...', extra=dados)
        for _ in range(int(qtyPackets)):
            requestClient, addr = serverSocket.recvfrom(1024)
            archive = archive + requestClient
        
        chekcsumServer = hashlib.sha1(archive).hexdigest()
        checksumEqual = bytearray(1)
        checksumEqual[0] = 2

        if chekcsumServer == checksumClient:

            with open(archiveDirectory, 'w+b') as archiveServer:
                archiveServer.write(archive)
            file = os.listdir(path='./archiveServer')
            if file.__contains__(fileName):
                nameLog.info('Protocol: %s', 'Download finished', extra=dados)
                checksumEqual[0] = 1
            else:
                nameLog.info('Protocol: %s', 'Download error !!', extra=dados)
                os.remove(archiveDirectory)
                checksumEqual[0] = 2
        else:
            nameLog.info('Protocol: %s', 'Download error !!', extra=dados)
            checksumEqual[0] = 2
        
        serverSocket.sendto(checksumEqual, addr)

if __name__ == "__main__":
    main()