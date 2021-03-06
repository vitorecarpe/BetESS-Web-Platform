import pika
import uuid
import threading

def send_message(message, bet_queue='bet_queue'):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()
    
    channel.basic_publish(
        exchange='',
        routing_key=bet_queue,
        properties=pika.BasicProperties(
            delivery_mode = 2, # make message persistent
        ),
        body=message)

    connection.close()