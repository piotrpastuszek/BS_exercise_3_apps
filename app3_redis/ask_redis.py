from itertools import count
import redis
import yaml
import yaml.loader
from flask import Flask

app = Flask(__name__)

with open('config.yml') as configuration:
    data = yaml.load(configuration, Loader=yaml.FullLoader)

HOST = data['HOST']
PORT = data['PORT']

@app.route('/size', methods=['GET'])
def get_redis_size():

    r = redis.Redis(
        host=HOST,
        port=PORT)

    count = redis.Redis()
    size = count.dbsize()
    size_msg = str(size)

    return size_msg

if __name__ == '__main__':
    app.run(debug=True)