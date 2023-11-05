#!/usr/bin/env python3
"""0. Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """Basic Cache class
    """
    def __init__(self):
        """initialization
        """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache
        """
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
