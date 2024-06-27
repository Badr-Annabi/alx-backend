#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This class LRUCache is a caching system for LRU"""

    def put(self, key, item):
        """
        Add new item while removing the first item
        if it exceeds the MAX_ITEMS
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(lru_key))
            self.cache_data.pop(lru_key)
        self.cache_data[key] = item

    def get(self, key):
        """Get item using its key"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
