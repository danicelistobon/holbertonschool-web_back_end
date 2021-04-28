#!/usr/bin/env python3
""" Redis basic module
"""
from redis.client import Redis
from uuid import uuid4
from typing import Union, Optional, Callable
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Takes a single method Callable argument and returns a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Create and return function that increments the count for that key
            every time the method is called and returns the value returned by
            the original method
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store the history of inputs and outputs for a particular function
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Retrieve the output. Store the output using rpush in the outputs
            list, then return the output
        """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """ Display the history of calls of a particular function
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Store an instance of the Redis client as a private variable
            named _redis
        """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes a data argument and returns a string
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """ Take a key string argument and an optional Callable argument
            named fn
        """
        if key:
            result = self._redis.get(key)
            if fn:
                return fn(result)
            else:
                return result

    def get_str(self, data: bytes) -> str:
        """ Will automatically parametrize Cache.get with the correct
            conversion function
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Will automatically parametrize Cache.get with the correct
            conversion function
        """
        byte_order = sys.byteorder
        return int.from_bytes(data, byte_order)
