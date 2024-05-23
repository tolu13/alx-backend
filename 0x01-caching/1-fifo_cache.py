#!/usr/bin/env python3
"""
a class FIFOCache that inherits from BaseCaching and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the
key key.
If key or item is None, tis method should not do anything.
If the number of items in self.cache_data is higher than
that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key

"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class fifo """

    def __init__(self):
        """ initialize """
        super().__init__()

    def put(self, key, item):
        """ assign to dict """

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
