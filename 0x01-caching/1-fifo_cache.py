#!/usr/bin/env python3
"""
a program that uses FIFO to cache entries
"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    a class that implements FIFO Caching
    """

    def __init__(self):
        """
        initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """retrieves an item by its key"""
        return self.cache_data.get(key, None)
