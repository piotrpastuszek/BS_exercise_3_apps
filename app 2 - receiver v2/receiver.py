from inspect import ismemberdescriptor
import pika
import sys
import os
import yaml
import json
import redis
from redis.commands.json.path import Path
from yaml.loader import SafeLoader
from multiprocessing import connection

with open('config.yml') as configuration:
    data = yaml.load(configuration, Loader=yaml.FullLoader)

HOST = data['HOST']
QUEUE = data['QUEUE']

REDIS_HOST = data['REDIS_HOST']
REDIS_PORT = data['REDIS_PORT']

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE, durable=True)

    def callback(ch, method, properties, body):
        print(body)
        object = json.loads(body)
        print(object)

        def pass_to_redis():
            try:
                r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
                r.set('msg_from_rabbitmq', json.dumps(object))
                r.expire('msg_from_rabbitmq', 60)
            except Exception as e:
                print(e)

        if __name__ == '__main__':
            pass_to_redis()

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