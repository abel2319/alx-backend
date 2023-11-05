#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Class LRU
    """
    def __init__(self):
        """initialization
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if item and key:
            if len(self.cache_data) == super().MAX_ITEMS and\
                    key not in self.cache_data.keys():
                discard = self.keys.pop(0)
                print(f'DISCARD: {discard}')
                self.cache_data.pop(discard)

            if key in self.cache_data.keys():
                self.keys.remove(key)

            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item by key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
