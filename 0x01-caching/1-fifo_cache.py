#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class FIFOCache is a caching system for FIFO"""

    def put(self, key, item):
        """
        Add new item while removing the first item
        if it exceeds the MAX_ITEMS
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))
        self.cache_data[key] = item

    def get(self, key):
        """Get item using its key"""
        if key is None:
            return None
        return self.cache_data.get(key)
