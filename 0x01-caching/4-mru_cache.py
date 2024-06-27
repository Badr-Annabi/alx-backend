#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This class MRUCache is a caching system for LRU"""

    def put(self, key, item):
        """
        Add new item while removing the most recent item
        if it exceeds the MAX_ITEMS
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))
        self.cache_data[key] = item

    def get(self, key):
        """Get item using its key"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
