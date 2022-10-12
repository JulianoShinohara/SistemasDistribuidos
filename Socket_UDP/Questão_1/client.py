################################################################################################################# 
# Questão 1 - UDP CLIENT                                                                                        #                                                                              #
# Descrição: Fazer um chat P2P que possibilite os clientes trocarem mensagens entre si                          #
#                                                                                                               #   
#   - tipo de mensagem [ 1 byte ]                                                                               #
#   - tamanho apelido (tam_apl) [ 1 byte ]                                                                      #
#   - apelido [ tam_apl ( 1 a 64 ) bytes]                                                                       #
#   - tamanho mensagem ( tam_msg ) [ 1 byte ]                                                                   #
#   - mensagem [ tam_msg bytes ]                                                                                #
#                                                                                                               #
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                             #
#   | Messagem Type | Nick Size | Nick [ Nick Size] ( 1-64 bytes) |                                             #
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                             #
#   | Messagem Type |   Message [ Message Size] ( 0-255 bytes)    |                                             #
#   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    
# Autores: Gabriela Marangoni Radigonda e Juliano Kendyi Shinohara                                              #
# Data de criação: 23/09/2022                                                                                   #
# Data de modificação: 25/09/2022 
#                      27/09/2022
#################################################################################################################

import socket
import emoji
import re
import sys
import threading

from emoji.core import emoji_count

HOST = "localhost"
PORT = [6000, 7000]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMessage(HOST, PORT):
    addr = HOST, PORT
    
    while True:
        print('Type your message here: ')
        message = input('> ')
        
        aux = len(message.encode())

        typeMsg = 1
        nicknameSize = len(nickname.encode())

        if aux < 256:  #verifica se a mensagem tem até um 255bytes
            if(emoji_count(emoji.demojize(message)) > 0): # se tem emoji
                typeMsg = 2
           
            if(urlMessage(message) != None): #se é url
                typeMsg = 3
          
            if(message.find("ECHO") == 0): #mensagem ECHO
                typeMsg = 4

            #formata
            
            message = (typeMsg.to_bytes(1,'big') + nicknameSize.to_bytes(1,'big') + nickname.encode() + aux.to_bytes(1,'big') + message.encode())
            clientSocket.sendto(message, addr)

        
        else: print('Too big. Try again!') #se tiver mais que 255bytes da erro


def receiveMessage(HOST, PORT):
    clientSocket.bind((HOST, int(PORT)))

    while True:
        message, addr = clientSocket.recvfrom(1024)
        typeMsg = int(message[0])
        print(typeMsg)
        nicknameSize = int(message[1])
        nickname = message[2:nicknameSize+2].decode() # apelido do cliente para a variavel nickname
        messageSize = message[nicknameSize+2]
        messagePosition = int(nicknameSize + 3)
        messageReceive = message[messagePosition : (messagePosition + messageSize)].decode()
      
        match typeMsg:
            case 1: #mensagem normal
                print(nickname + ' >> ' + messageReceive)
            
            case 2: #emoji
                print(nickname + ' >> ' + emoji.emojize(messageReceive))

            case 3: #URL
                print(nickname + ' >> Link: ' + messageReceive)

            case 4: #ECHO
                typeMsg = 1
                message = (typeMsg.to_bytes(1,'big') + nicknameSize.to_bytes(1,'big') + nickname.encode() + messageSize.to_bytes(1,'big') + messageReceive.encode())
                clientSocket.sendto(message, addr)
         

def urlMessage(url):
    regexp = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regexp, url)

def main():
    
    global nickname
    aux = sys.argv[1]

    while True:
        print('What nickname do you wanna use?')
        nickname = input('> ')
        nicknameSize = len(nickname.encode())

        if nicknameSize > 65  and nicknameSize < 1:
            print('Try again!')
        else: 
            break

    try:
        match aux: #criando 2 threads: uma para enviar e outra para receber as mensagens no chat
            case '1':
                threading.Thread(target=sendMessage, args=(HOST, PORT[0])).start()
                threading.Thread(target=receiveMessage, args=(HOST, PORT[1])).start()

            case '2':
                threading.Thread(target=sendMessage, args=(HOST, PORT[1])).start()
                threading.Thread(target=receiveMessage, args=(HOST, PORT[0])).start()

    except: print('ERROR!!')


if __name__ == "__main__":
    main()





