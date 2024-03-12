import pika, sys, os ,logging

AMQP_URL = 'amqps://vsuiygqg:3n2_5DsZNsMrpip6zwD28gP8Wl6ElcWt@cow.rmq2.cloudamqp.com/vsuiygqg'

logging.basicConfig(level=logging.INFO)

def recieve():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='song_id')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='song_id', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages.')
    channel.start_consuming()

recieve()