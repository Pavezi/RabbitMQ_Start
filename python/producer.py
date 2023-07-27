import pika

# Criar uma conexão
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar uma fila
channel.queue_declare(queue='hello')

# Publicar uma mensagem
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
