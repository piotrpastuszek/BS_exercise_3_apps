import pika
import yaml
import json
from flask import Flask
from yaml.loader import SafeLoader
from multiprocessing import connection

app = Flask(__name__)

with open('config.yml') as configuration:
    data = yaml.load(configuration, Loader=yaml.FullLoader)

FILE = data['FILE_PATH']
QUEUE = data['QUEUE']
HOST = data['HOST']
APP_HOST = data['APP_HOST']

@app.route('/add', methods=['POST'])
def get_data():
    
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
        except Exception as e:
            return print("Something went wrong")

        connection.close()
        return json_object

    except ValueError as error:
        error_message = "404 Bad Request"
        return error_message

    

if __name__ == '__main__':
    app.run(host=APP_HOST, debug=True)