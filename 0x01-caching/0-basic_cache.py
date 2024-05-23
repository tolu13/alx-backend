#!/usr/bin/env python3
"""
 class BasicCache that inherits from BaseCaching and is a caching system:
 This caching system doesn’t have limit
 def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None

"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a class called basecache """

    def __init__(self):
        """ init """
        super().__init__()

    def put(self, key, item):
        """ must assign to dict self cache """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
