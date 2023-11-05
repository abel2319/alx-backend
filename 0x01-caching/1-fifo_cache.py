#!/usr/bin/env python3
"""1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFO
    """
    def __int__():
        """initialization
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if item and key:
            if len(self.cache_data) == super().MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f'DISCARD: {first_key}')
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
