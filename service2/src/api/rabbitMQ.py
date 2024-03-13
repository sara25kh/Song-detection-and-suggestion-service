import pika
import logging

AMQP_URL = 'amqps://vsuiygqg:3n2_5DsZNsMrpip6zwD28gP8Wl6ElcWt@cow.rmq2.cloudamqp.com/vsuiygqg'

logging.basicConfig(level=logging.INFO)

def receive():
    song_info_list = []  # List to store received song info

    def callback(ch, method, properties, body):
        try:
            # Decode the received bytes and split the message using the delimiter
            song_info = body.decode('utf-8').split('|')
            print(f" [x] Received song info: {song_info}")
            song_info_list.append(song_info)  # Append to the list
        except Exception as e:
            logging.error(f"Error in processing message: {e}")

    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()
    channel.queue_declare(queue='song_id')

    channel.basic_consume(queue='song_id', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages.')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        connection.close()
        print(" [*] Stopped consuming messages.")

    return song_info_list  # Return the list after consuming messages

# Example usage:
# song_info_list = receive()
# print(song_info_list)












# import pika, sys, os ,logging

# AMQP_URL = 'amqps://vsuiygqg:3n2_5DsZNsMrpip6zwD28gP8Wl6ElcWt@cow.rmq2.cloudamqp.com/vsuiygqg'

# logging.basicConfig(level=logging.INFO)

# def recieve():
#     connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
#     channel = connection.channel()
#     channel.queue_declare(queue='song_id')

#     def callback(ch, method, properties, body):
#         try:
#             # Decode the received bytes and split the message using the delimiter
#             song_info = body.decode('utf-8').split('|')
#             print(f" [x] Received song info: {song_info}")
#             # Return individual elements of the list separately
#             return song_info
#         except Exception as e:
#             logging.error(f"Error in processing message: {e}")
#             return None

#     channel.basic_consume(queue='song_id', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages.')
#     try:
#         channel.start_consuming()
#     except KeyboardInterrupt:
#         connection.close()
#         print(" [*] Stopped consuming messages.")

# # recieve()
# song_info = recieve()
# print(song_info)
