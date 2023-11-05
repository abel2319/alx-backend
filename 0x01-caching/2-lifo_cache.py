#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class LIFO
    """

    def __int__():
        """initialization
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """Add an item in the cache
        """
        if item and key:
            if len(self.cache_data) == super().MAX_ITEMS and\
                    key not in self.cache_data.keys():
                print(f'DISCARD: {self.last_key}')
                self.cache_data.pop(self.last_key)

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """Get an item by key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
