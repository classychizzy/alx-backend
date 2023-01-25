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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, Last=True)


    def get(self, key):
        """retrieves an item from the cache"""
        return self.cache_data.get(key, None)
