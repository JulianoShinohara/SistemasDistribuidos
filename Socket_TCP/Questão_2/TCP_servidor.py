###############################################################################
# Questão 2 - TCP Servidor                                                    #
# Descrição:  Faça uma aplicação com um servidor que gerencia um conjunto de  #
# arquivos remotos entre múltiplos usuários. O servidor deve responder aos    #
# seguintes comandos:                                                         #
#              -> ADDFILE (1): adiciona um arquivo novo.                      #
#              -> DELETE (2): remove um arquivo existente.                    #
#              -> GETFILESLIST (3): retorna uma lista com o nome dos arquivos #
#              -> GETFILE (4): faz download de um arquivo.                    #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara            #
# Data de criação: 11/09/2022                                                 #
# Datas de atualizações: 18/09/2022                                           #
#                        20/09/2022                                           #
###############################################################################

import logging
import os
import socket
import threading

HOST = ""
PORT = 6000
addr = (HOST, PORT)

# Cria socket e define a instancia
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(addr)

# Define o formato do log
formatLog = '%(asctime)-1s %(userIP)s %(userPort)s %(message)s'
logging.basicConfig(format=formatLog, level=20)
nameLog = logging.getLogger('TCP_Server')


def connectionClient(ip, port, connection):
    dados = {'userIP': ip, 'userPort': port}

    while True:
        responseHeader = bytearray(3)
        responseHeader[0] = 2

        # Recebe e separa os campos do cabeçalho
        messageReceived = bytearray(connection.recv(1024))
        messageType = int(messageReceived[0])
        commandIdent = int(messageReceived[1])
        fileNameSize = int(messageReceived[2])
        fileName = messageReceived[3:].decode('utf-8')

        # ADD FILE
        match commandIdent:
            case 1:
                nameLog.info('Protocol: %s',
                             'Received ADDFILE request', extra=dados)
                archiveSize = int.from_bytes(
                    connection.recv(4), byteorder='big')
                archive = b''
                nameLog.info('Protocol: %s', ' Downloading...', extra=dados)
                archive = connection.recv(archiveSize)
                nameLog.info('Protocol: %s', ' Download finished', extra=dados)

                with open('./archiveServer/' + fileName, 'w+b') as archiveFile:
                    archiveFile.write(archive)

                archive = os.listdir(path='./archiveServer/')
                if fileName in archive:
                    responseHeader[2] = 1
                    nameLog.info('Protocol: %s',
                                 'Successfully ADDFILE', extra=dados)
                else:
                    responseHeader[2] = 2
                    nameLog.info('Protocol: %s',
                                 'Unsuccessfully ADDFILE', extra=dados)

                responseHeader[1] = 1
                connection.send(responseHeader)
                nameLog.info('Protocol: %s',
                             'Response ADDFILE sent', extra=dados)

            # DELETE archive
            case 2:
                nameLog.info('Protocol: %s',
                             'Received DELETE request', extra=dados)
                if os.path.isfile('./archiveServer/' + fileName):
                    os.remove('./archiveServer/' + fileName)

                    if os.path.isfile('./archiveServer/' + fileName):
                        responseHeader[2] = 2
                        nameLog.info('Protocol: %s',
                                     'Unsuccessfully DELETE ', extra=dados)
                    else:
                        responseHeader[2] = 1
                        nameLog.info('Protocol: %s',
                                     'Successfully DELETE ', extra=dados)

                connection.send(responseHeader)
                nameLog.info('Protocol: %s',
                             'Response DELETE sent ', extra=dados)

            # GETFILESLIST
            case 3:

                nameLog.info('Protocol: %s',
                             'Received GETFILESLIST request', extra=dados)
                quantityFiles = 0
                files: list[str] = []
                directory = os.listdir('./archiveServer/')
                responseHeader[1] = 3
                nameSizeResponseHeader = 0

                for nameFile in directory:
                    if os.path.isfile(str('./archiveServer/' + nameFile)):
                        quantityFiles = quantityFiles + 1
                        files.append(str(nameFile))

                if quantityFiles > 0:
                    responseHeader[2] = 1
                    connection.send(responseHeader)
                    connection.send(quantityFiles.to_bytes(2, byteorder="big"))
                    for nameFile in files:
                        nameSizeResponseHeader = len(nameFile)
                        connection.send(
                            nameSizeResponseHeader.to_bytes(1, byteorder="big"))
                        connection.send(nameFile.encode())
                        nameLog.info('Protocol: %s',
                                     'Response GETFILELIST sent', extra=dados)

                else:
                    nameLog.info('Protocol: %s',
                                 'Unsucessfully GETFILELIST', extra=dados)
                    responseHeader[2] = 2
                    connection.send(responseHeader)
                    nameLog.info('Protocol: %s',
                                 'Response GETFILELIST sent', extra=dados)

            # GETLIST
            case 4:
                nameLog.info('Protocol: %s',
                             'Received GETLIST request', extra=dados)
                responseHeader[1] = 4
                archive = os.listdir('./archiveServer/')

                if len(fileName) <= 255:
                    responseHeader[2] = 1
                    connection.send(responseHeader)
                    nameLog.info('Protocol: %s',
                                 'Response GETLIST sent', extra=dados)
                    fileSize = (os.stat('./archiveServer/' +
                                fileName).st_size).to_bytes(4, byteorder="big")
                    connection.send(fileSize)
                    fileOpen = open('./archiveServer/' + fileName, 'rb')
                    file = fileOpen.read()
                    nameLog.info('Protocol: %s',
                                 'Starting upload', extra=dados)
                    connection.send(file)
                    nameLog.info('Protocol: %s',
                                 'Upload finished', extra=dados)
                    fileOpen.close()

                else:
                    nameLog.info('Protocol: %s',
                                 'Unsuccessfully GETFILE', extra=dados)
                    responseHeader[2] = 2
                    connection.send(responseHeader)
                    nameLog.info('Protocol: %s',
                                 'Response GETFILE sent', extra=dados)


def main():
    vetorThreads = []

    while True:
        serverSocket.listen(3)
        (connection, (ip, port)) = serverSocket.accept()
        dados = {'userIP': ip, 'userPort': port}
        nameLog.info('Protocol info: %s',
                     'connection established', extra=dados)

        thread = threading.Thread(
            target=connectionClient, args=(ip, port, connection, ))
        thread.start()
        vetorThreads.append(thread)


if __name__ == "__main__":
    main()
