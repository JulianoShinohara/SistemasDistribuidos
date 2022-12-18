import pika as pk
import sys

def main(): 
    # Coneta ao servidor RabbitMQ
    connection = pk.BlockingConnection(pk.ConnectionParameters(host='localhost')) 
    channel = connection.channel() # Cria um canal de comunicação
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct') # Cria um exchange do tipo topic

    result = channel.queue_declare(queue='', exclusive=True) # Cria uma fila exclusiva 
    queueName = result.method.queue # Pega o nome da fila

    queues = ["people", "beautiful", "actor", "Fasting", "innovation", "house", "alone"] # Lista de filas
    topics = sys.argv[1:] # Lista de tópicos

    if not topics: # Se não houver tópicos
        sys.stderr.write("Registra-se em algum dos tópicos a seguir: people, beautiful, actor, Fasting, innovation, lesson, alone") 
        sys.exit(1)

    for i in range(len(topics)): # Para cada tópico
        if topics[i] not in queues: # Se o tópico não estiver na lista de filas
            sys.stderr.write("Tópico inválido. Registra-se em algum dos tópicos a seguir: people, beautiful, actor, Fasting, innovation, lesson, alone")
            sys.exit(1)
    
    # Crio a fila dado o topico
    for topico in topics:
        channel.queue_bind(exchange='direct_logs', queue=queueName, routing_key=topico)

    print("*** Aguardando mensagens. Para sair, pressione CTRL+C ***") # Mensagem de aguardo

    def callback(ch, method, properties, body): # Função de callback para exibir o resultado
        data = body.decode()
        print(" Tópico: %r" % (method.routing_key)) # Imprime a mensagem
        print(data) # Imprime o tópico
        print("***------------------------***")

    channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True) # Associa a função de callback à fila
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Finalizando o programa...")