#!/usr/bin/env python3
"""
    This module contains a class that inherits from BaseCaching and is
    a basic LRUCache - Least Recently used
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        This Class is a basic Caching system that imports from
        BaseCaching. It uses the Least recently usage Caching approach

        Methods:
            put: this method is used to add a new cache to the cache system
            get: this is used to get the cache data from the cache system
    """
    def __init__(self):
        """
            This is the initialization the class instance
        """
        super().__init__()
        # this is the least Recent Cache Usage
        self.lru = []

    def put(self, key=None, item=None):
        """
            This Method is used store a data to the cache_data dictionary

            This method uses the Least recently used caching approach.
            When a new item is added it is appended to the end of the
            self.lru(Least recently used)

            if the caching storage is full It will use the first element in the
            self.lru to know which element is the least recently used

            Arguments:
                key: this is the key identifier(Str)
                item: this is the value to be assigned
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            length_data = len(self.cache_data)
            if length_data > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.lru[0]]
                print(f"DISCARD: {self.lru[0]}")
                del self.lru[0]
            if key not in self.lru:
                self.lru.append(key)

    def get(self, key=None):
        """
            This method is used to get the value of a key from the cache_data

            This method uses the Least recently used algorithm.
            On trying to get an element It removes it from the `self.lru`
            because it is not more the Least recently used but not the last
            Recently used. This is why it is added to the end of the list.

            Arguments:
                key: this is the key identifier(Str)

            Return: returns the value assigned to the key or None if not exists
        """

        value = self.cache_data.get(key)
        if key in self.lru and len(self.lru) > 1:
            self.lru.remove(key)
            self.lru.append(key)
        return value
