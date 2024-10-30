#!/usr/bin/env python3
"""
    This Module contains a class BasicCache that inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        This Class is a Basic caching system

        Methods:
            get: this method is used to retrieve an item
            put: this method is used to store an item
            print_cache: This is an inherited method that is used to print the
                         stored data
    """
    def __init__(self):
        """
            This is the initialization of the Instance of the BasicCache
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

    def get(self, key=None):
        """
            This method is used to get the value of a key from the cache_data

            Arguments:
                key: this is the key identifier(Str)

            Return: returns the value assigned to the key or None if not exists
        """
        return self.cache_data.get(key)
