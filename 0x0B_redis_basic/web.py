#!/usr/bin/env python3
""" Expiring web cache and tracker module
"""
from redis.client import Redis
from typing import Callable
from functools import wraps
import requests


def count_calls(method: Callable) -> Callable:
    """ Takes a single method Callable argument and returns a Callable
    """
    redis = Redis()

    @wraps(method)
    def wrapper(url):
        """ Function wrapper count calls
        """
        redis.incr(f'count:{url}')
        res = redis.get(url)
        if res:
            return res.decode("utf-8")
        result = method(url)
        redis.setex(url, 10, result)
        return result
    return wrapper


@count_calls
def get_page(url: str) -> str:
    """ The core of the function is very simple. It uses the requests module to
        obtain the HTML content of a particular URL and returns it
    """
    res = requests.get(url)
    return res.text
