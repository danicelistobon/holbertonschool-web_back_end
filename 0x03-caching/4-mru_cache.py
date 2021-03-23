#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.head, self.tail = 'head', 'tail'
        self.next, self.prev = {}, {}
        self.connect(self.head, self.tail)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def _remove(self, key):
        """ Remove an item from the cache
        """
        self.connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def connect(self, x, y):
        """ Connect items
        """
        self.next[x], self.prev[y] = y, x

    def _add(self, key, item):
        """ Add an item in the cache
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.prev[self.tail]))
            self._remove(self.prev[self.tail])
        self.cache_data[key] = item
        self.connect(self.prev[self.tail], key)
        self.connect(key, self.tail)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            val = self.cache_data[key]
            self._remove(key)
            self._add(key, val)
            return val
