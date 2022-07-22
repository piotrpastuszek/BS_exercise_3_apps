from inspect import ismemberdescriptor
import pika
import sys
import os
import yaml
import json
from yaml.loader import SafeLoader
from multiprocessing import connection

with open('config.yml') as configuration:
    data = yaml.load(configuration, Loader=yaml.FullLoader)

HOST = data['HOST']
QUEUE = data['QUEUE']

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE, durable=True)

    def callback(ch, method, properties, body):
        print(body)
        json_object = json.loads(body)
        print(json_object)

    channel.basic_consume(queue=QUEUE, on_message_callback=callback, auto_ack=True)

    print('Listening')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)