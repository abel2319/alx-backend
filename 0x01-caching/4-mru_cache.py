#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Class MRU
    """
    def __init__(self):
        """initialization
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            if key in self.stack:
                self.stack.remove(key)

            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
