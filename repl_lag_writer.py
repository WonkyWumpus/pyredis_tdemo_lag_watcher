#!/usr/bin/env python3
import redis
from time import (time, sleep)

milliseconds = lambda: int(time() * 1000)

redis = redis.Redis(
host='localhost',
port=6379,
password='')

while (1):
  redis.set('ReplLagTest', milliseconds())
  sleep(.5)
