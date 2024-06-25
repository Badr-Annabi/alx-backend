#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class LIFOCache is a caching system for LIFO"""

    def put(self, key, item):
        """
        Add new item while removing the first item
        if it exceeds the MAX_ITEMS
        """
        if key is None or item is None:
            return
        if (
            len(self.cache_data) >= self.MAX_ITEMS) and (
                key not in self.cache_data):
            last_item = next(reversed(self.cache_data))
            del self.cache_data[last_item]
            print("DISCARD: {}".format(last_item))
        self.cache_data[key] = item

    def get(self, key):
        """Get item using its key"""
        if key is None:
            return None
        return self.cache_data.get(key)
