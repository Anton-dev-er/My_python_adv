import pika

from pika import PlainCredentials

# это просто синтаксис для создания подключения к Кролику
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# создаём канал для передачи данных
channel = connection.channel()

data = {"1": 1,
        "2": 2}

channel.basic_publish(exchange='',
                      routing_key='test_queue',
                      body=f"{data}".encode())
print("OK")
connection.close()