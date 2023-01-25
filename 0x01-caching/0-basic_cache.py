#!/usr/bin/env python3
"""
a program that implements basic caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a class that caches data
    """
    def put(self, key, item):
        """ a function that adds key and value
        to the cache_data
        """
        self.cache_data[key] = item
        if key is None or item is None:
            return

    def get(self, key):
        """
        returns the value linked to a key
        """
        return self.cache_data.get(key, None)
