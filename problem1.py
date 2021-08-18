from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.max_size=capacity
        self.cache = OrderedDict()  # last elements are oldest

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
        	self.cache.move_to_end(key, last=False)
        	return self.cache[key]
        else:
        	return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        # Key is already in dictionary
        if key in self.cache:
        	self.cache[key]=value
        	self.cache.move_to_end(key, last=False)

        # Key is not in dictionary
        else:
        	# Add the key-value pair when the dictionary is full
        	if len(self.cache)>=self.max_size:
        		self.cache.popitem()
        		self.cache[key]=value
        		self.cache.move_to_end(key, last=False)

        	# Add the key-value pair when the dictionary is not full
        	else:
        		self.cache[key]=value
        		self.cache.move_to_end(key, last=False)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache


our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry