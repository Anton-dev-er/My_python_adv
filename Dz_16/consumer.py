import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test_queue', durable=True)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    body.decode()
    ch.basic_ack(delivery_tag=method.delivery_tag)
    save(body)


def save(data):
    data = data.decode('utf8').replace("'", '"')
    data = json.loads(data)
    e = Employees.query.get(data["creator_id"])
    O = Orders(order_type=data["order_type"],
                            descriptions=data["descriptions"],
                            status=data["status"],
                            serial_no=data["serial_no"],
                            creator_id=e.creator_id)
    db.session.add(O)
    db.session.commit()


channel.basic_consume(on_message_callback=callback,
                      queue='test_queue',
                      auto_ack=False)

channel.start_consuming()