import pika
import yaml
import json
from yaml.loader import SafeLoader
from multiprocessing import connection

with open('config.yml') as configuration:
    data = yaml.load(configuration, Loader=yaml.FullLoader)

FILE = data['FILE_PATH']
QUEUE = data['QUEUE']
HOST = data['HOST']


with open(FILE, 'r') as f:
    json_object = f.read()

try:
    json_string = json.loads(json_object)


    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    try:
        channel.queue_declare(queue=QUEUE, durable=True)

        channel.basic_publish(
                            exchange='', 
                            routing_key=QUEUE, 
                            body=json_object,
                            )
            
        print("Sent succesfully")
    except Exception as e:
        print("Something went wrong")

    connection.close()

except ValueError as error:
    print("404 Bad Request")