from itertools import count
import redis
import yaml
import yaml.loader

with open('config.yml') as configuration:
    data = yaml.load(configuration, Loader=yaml.FullLoader)

HOST = data['HOST']
PORT = data['PORT']

r = redis.Redis(
    host=HOST,
    port=PORT)

count = redis.Redis()
size = count.dbsize()

print(size)