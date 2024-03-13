import pika, sys, os ,logging

AMQP_URL = 'amqps://vsuiygqg:3n2_5DsZNsMrpip6zwD28gP8Wl6ElcWt@cow.rmq2.cloudamqp.com/vsuiygqg'

logging.basicConfig(level=logging.INFO)

def send(song_info):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='song_id')

    # body = '|'.join(song_info)
    body = '|'.join(str(item) for item in song_info)
    
    channel.basic_publish(exchange='',
                      routing_key='song_id',
                      body=body.encode('utf-8'))
    logging.info(f'song {song_info} has been sent to rabbitMQ')

    connection.close()


# send(['13','song'])