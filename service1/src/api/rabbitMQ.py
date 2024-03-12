import pika, sys, os ,logging

AMQP_URL = 'amqps://vsuiygqg:3n2_5DsZNsMrpip6zwD28gP8Wl6ElcWt@cow.rmq2.cloudamqp.com/vsuiygqg'

logging.basicConfig(level=logging.INFO)

def send(songID):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='song_id')

    channel.basic_publish(exchange='',
                      routing_key='song_id',
                      body=str(songID))
    logging.info(f'song {songID} has been sent to rabbitMQ')

    connection.close()


send('123')