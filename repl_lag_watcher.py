import redis
from time import (time, sleep)

milliseconds = lambda: int(time() * 1000)

redis = redis.Redis(
host='localhost',
port=6379,
password='')

result = ''
old_result = ''

while (1):
  mymillis = milliseconds()
  result = redis.get('ReplLagTest')
  if (old_result != result):
    print((mymillis - int(result.decode('utf-8'))))
  old_result = result
  sleep(.01)

