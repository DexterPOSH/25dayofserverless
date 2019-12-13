import redis
import os

REDISCLIENT = redis.Redis(
    host=os.environ['REDIS_HOSTNAME'],
    port= 6380,
    password=os.environ['REDIS_PASSWORD'],
    ssl=True
)

def getValueFromCache(key: str):
    global REDISCLIENT
    return REDISCLIENT.get(key)

def setValueInCache(key: str, value: str):
    global REDISCLIENT
    return REDISCLIENT.set(key, value)
