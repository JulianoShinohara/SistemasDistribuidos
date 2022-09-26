###############################################################################
# Questão 2 - TCP Cliente                                                     #
# Descrição:  Faça uma aplicação com um servidor que gerencia um conjunto de  #
# arquivos remotos entre múltiplos usuários. O servidor deve responder aos    #
# seguintes comandos:                                                         #
#              -> ADDFILE (1): adiciona um arquivo novo.                      #
#              -> DELETE (2): remove um arquivo existente.                    #
#              -> GETFILESLIST (3): retorna uma lista com o nome dos arquivos #
#              -> GETFILE (4): faz download de um arquivo.                    #
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara           #
# Data de criação: 11/09/2022                                                 #
# Datas de atualizações: 18/09/2022                                           #
#                        20/09/2022                                           #
###############################################################################

import os
import socket

HOST = "localhost"
PORT = 6000
addr = (HOST, PORT)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
clientSocket.connect(addr)


def main():
    while True:
        var = input(">  ")
        varFormated = ''
        header = bytearray(3)
        header[0] = 1

        if (len(var.split())) > 1:
            fileName = var.split()[1]
            varFormated = var.split()[0].upper()

        else:
            varFormated = var.upper()

        match varFormated:
            case 'ADDFILE':

                header[1] = 1
                header[2] = len(fileName)
                size = len(fileName)
                file = os.listdir('./files')

                if (file.__contains__(fileName)):
                    if (size < 256):
                        clientSocket.send(header + bytearray(fileName.encode()))
                        # tamanho do arquivo transformado em bytes e faz a ordenação usando Big Endian
                        fileSize = (
                            os.stat('./files/' + fileName).st_size).to_bytes(4, 'big')
                        clientSocket.send(fileSize)
                        OpenFile = open('./files/' + fileName,
                                        'rb')  # leitura binária
                        fileBytes = OpenFile.read()  # arquivo se transforma em byte
                        clientSocket.send(fileBytes)

                        confirmation = int(clientSocket.recv(3)[2])
                        if (confirmation == 1):
                            print('File added!')

                        else:
                            print('ERROR adding a file!')

                else:
                    print('ERROR: already exists!')

            case 'DELETE':

                header[1] = 2
                header[2] = len(fileName)
                clientSocket.send(header + bytearray(fileName.encode()))

                # confirmação se deu certo ou não o deletar
                confirmation = int(clientSocket.recv(3)[2])
                if (confirmation == 1):
                    print('File deleted!')

                else:
                    print('ERROR deleting a file!')

            case 'GETFILESLIST':

                header[1] = 3
                header[2] = 0
                clientSocket.send(header)

                if (clientSocket.recv(3)[2] == 1):
                    quantityFiles = int.from_bytes(clientSocket.recv(2), 'big')
                    print('Files: [', quantityFiles, ']')
                    for _ in range(quantityFiles):
                        fileSize = int.from_bytes(clientSocket.recv(1), 'big')
                        print(clientSocket.recv(fileSize).decode())

                else:
                    print('ERROR getting file list!')

            case 'GETFILE':

                header[1] = 4
                header[2] = len(fileName)
                clientSocket.send(header + bytearray(fileName.encode()))

                if (clientSocket.recv(3)[2] == 1):
                    sizeFileBig = int.from_bytes(
                        clientSocket.recv(4), byteorder='big')
                    file = b''  # define arquivo para bytes
                    file = clientSocket.recv(sizeFileBig)

                    with open('./files/' + fileName, 'w+b') as files:
                        files.write(file)
                    print('Get file with SUCCESS!')

                else:
                    print('ERROR getting file!')


if __name__ == "__main__":
    main()
