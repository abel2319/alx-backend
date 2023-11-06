#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class LFU
    """
    def __init__(self):
        """initialization
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_order:
                self.cache_order.append(key)
            else:
                self.cache_order.remove(key)
                self.cache_order.append(key)
            if len(self.cache_order) > BaseCaching.MAX_ITEMS:
                popped = self.cache_order.pop(0)
                del self.cache_data[popped]
                print("DISCARD: {}".format(str(popped)))

    def get(self, key):
        """Get an item by key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
