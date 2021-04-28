#!/usr/bin/env python3
""" Redis basic module
"""
from redis.client import Redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Store an instance of the Redis client as a private variable
            named _redis
        """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes a data argument and returns a string
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
