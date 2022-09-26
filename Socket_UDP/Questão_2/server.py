######################################################################################### 
# Questão 2 - UDP CLIENT                                                                #                                                                              #
# Descrição:                                                                            #
#   Servidor recebe um arquivo do cliente e verifica se o checksum é identico ao local. #   
#                                                                                       #   
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                      #
# Data de criação: 23/09/2022                                                           #
# Data de modificação: 25/09/2022                                                       #
#########################################################################################

import math
import socket
import os
import logging
import hashlib

HOST = "127.0.0.1"
PORT = 6000
addr = (HOST, PORT)

# Cria socket e define a instancia
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)

# Define o formato do log
formatLog = '%(asctime)-1s %(userIP)s %(userPort)s %(message)s'
logging.basicConfig(format=formatLog, level=20)
nameLog = logging.getLogger('UDPServer')

def main():
    while True:
        requestClient, addr = serverSocket.recvfrom(1024)
        dados = {'userIP': addr[0], 'userPort': addr[1]}
        fileSize = int.from_bytes(requestClient, addr = serverSocket.recvfrom(1024) [:4], byteorder = 'big')
        fileName = requestClient[4:].decode()
        qtyPackets = math.ceil(fileSize/1024)
        nameLog.info('Protocol: %s', 'Downloading...', extra=dados)
        file = open('./archiveServer/' + fileName, 'w+b')

        for i in range(qtyPackets):
            inf, addr = serverSocket.recvfrom(1024)
            file.write(inf)

        file.seek(0)

        chekcsumServer = hashlib.sha1(file.read()).hexdigest()
        checksumClient, addr = serverSocket.recvfrom(1024)
        checksumClient = checksumClient.decode()

        if chekcsumServer == checksumClient:
            nameLog.info('Protocol: %s', 'Download finished', extra=dados)
            file.close()
        else:
            nameLog.info('Protocol: %s', 'Download error !!', extra=dados)
            os.remove('./archiveServer/' + fileName)
            file.close()

if __name__ == "__main__":
    main()