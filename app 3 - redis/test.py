from itertools import count
import redis

r = redis.Redis(
    host='localhost',
    port=6379)

count = redis.Redis()
size = count.dbsize()

print(size)