#!/usr/bin/env python3
"""
a program that uses LIFO Caching
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    a class that implements base caching
    """
    def __init__(self):
        """initializes the caching system
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(key, item):
        """ adds a new item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", last_key)

    def get(self, key):
        """retrieves an item from the cache"""
        return self.cache_data.get(key, None)
