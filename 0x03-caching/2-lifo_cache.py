#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
