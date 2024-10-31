#!/usr/bin/env python3
"""
    This module contains a class that inherits from BaseCaching and is
    a basic LFUCache - Least Frequently used
"""
from base_caching import BaseCaching


def return_lfu(lfu):
    """
        This method is used to return the least recently used element
    """
    least_value = min(list(lfu.values()))
    for key, value in lfu.items():
        if value == least_value:
            return key


class LFUCache(BaseCaching):
    """
        This Class is a basic Caching system that imports from
        BaseCaching. It uses the Least Frequently usage Caching approach

        Methods:
            put: this method is used to add a new cache to the cache system
            get: this is used to get the cache data from the cache system
    """
    def __init__(self):
        """
            This is the initialization the class instance
        """
        super().__init__()
        # this is the least Frequently Used Cache
        self.lfu = {}

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
                lfu = return_lfu(self.lfu)
                del self.cache_data[lfu]
                print(f"DISCARD: {lfu}")
                del self.lfu[lfu]
            if key not in self.lfu.keys():
                self.lfu[key] = 0

    def get(self, key=None):
        """
            This method is used to get the value of a key from the cache_data
            Arguments:
                key: this is the key identifier(Str)

            Return: returns the value assigned to the key or None if not exists
        """

        value = self.cache_data.get(key)
        if key in self.lfu.keys():
            self.lfu[key] += 1
        return value
