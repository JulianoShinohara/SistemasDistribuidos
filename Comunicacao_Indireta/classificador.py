import pika as pk

def main():
    # Abre conexão com o RabbitMQ
    connection = pk.BlockingConnection(pk.ConnectionParameters(host='localhost'))

    # Conecta o canal
    channel = connection.channel()

    # Declara a fila
    channel.queue_declare(queue='tweets')

    def callback(ch, method, properties, body):
        # Variavel para armazenar o topico
        topic = ''

        # Decodifica o dataset
        data = body.decode()

        # Verifica se tweets contém alguma das palavras chaves
        if 'people' in data:
            topic = 'people'
        elif 'beautiful' in data:
            topic = 'beautiful'
        elif 'Fasting' in data:
            topic = 'Fasting'
        elif 'innovation' in data:
            topic = 'innovation'
        elif 'saudade' in data:
            topic = 'saudade'
        elif 'house' in data:
            topic = 'house'
        elif 'alone' in data:
            topic = 'alone'
        # Canal utilizado para comunicação entre classificador de cliente
        channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
        # Envia o topico para a fila do tweet
        channel.basic_publish(exchange='direct_logs', routing_key=str(topic), body=body) # Publica a mensagem no topico
    
    # Cria a base da comunicação
    channel.basic_consume(queue = 'tweets', on_message_callback = callback, auto_ack = True)
    # Inicia a comunicação
    channel.start_consuming() 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Finalizando o programa...")