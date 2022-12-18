import pika as pk
import csv

def main():
    # Conecta ao servidor RabbitMQ
    connection = pk.BlockingConnection(pk.ConnectionParameters('localhost')) 
    channel = connection.channel() # Cria um canal de comunicação

    file = open('./dataset/ElonTweets.csv', errors='ignore') #local do csv
    data = csv.DictReader(file) # lê o arquivo csv

    for dataAux in data:
        user = "Username: " + dataAux["Username"] #armazena o userName do csv de quem escreveu o tweet
        text = "Text: " + dataAux["Text"] #armazena o texto do tweet
        dataUser = user + " \n" + text + "\n\n" #concatena o userName e o texto do tweet
        channel.exchange_declare(exchange='tweets', exchange_type='direct') #troca de mensagens
        channel.basic_publish(exchange='', routing_key='tweets', body=dataUser) #publica a mensagem

    connection.close() #fecha a conexão

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Finalizando o programa...")