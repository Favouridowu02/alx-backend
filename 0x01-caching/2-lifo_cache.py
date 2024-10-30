#!/usr/bin/env python3
"""
    This module contains a class that inherits from BaseCaching and is
    a basic LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        This Class is a basic Caching system that imports from
        BaseCaching

        Methods:
            put: this method is used to add a new cache to the cache system
            get: this is used to get the cache data from the cache system
    """
    def __init__(self):
        """
            This is the initialization the class instance
        """
        super().__init__()
        self.last_cache = None

    def put(self, key=None, item=None):
        """
            This Method is used store a data to the cache_data dictionary

            Arguments:
                key: this is the key identifier(Str)
                item: this is the value to be assigned
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            length_data = len(self.cache_data)
            if length_data > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.last_cache]
                print(f"DISCARD: {self.last_cache}")
            self.last_cache = key

    def get(self, key=None):
        """
            This method is used to get the value of a key from the cache_data

            Arguments:
                key: this is the key identifier(Str)

            Return: returns the value assigned to the key or None if not exists
        """
        return self.cache_data.get(key)