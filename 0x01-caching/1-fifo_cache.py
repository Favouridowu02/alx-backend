#!/usr/bin/env python3
"""
    This module contains a class that inherits from BaseCaching and is
    a basic FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        This Class is a basic Caching system that imports from
        BaseCaching

        Methods:
    """
    def __init__(self):
        """
            This is the initialization the class instance
        """
        super().__init__()

    def put(self, key=None, item=None):
        """
            This Method is used store a data to the cache_data dictionary

            Arguments:
                key: this is the key identifier(Str)
                item: this is the value to be assigned
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key=None):
        """
            This method is used to get the value of a key from the cache_data

            Arguments:
                key: this is the key identifier(Str)

            Return: returns the value assigned to the key or None if not exists
        """
        return self.cache_data.get(key)
