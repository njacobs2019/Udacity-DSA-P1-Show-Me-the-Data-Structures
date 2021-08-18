from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.max_size=capacity
        self.cache = OrderedDict()  # last elements are oldest

    def get(self, key=None):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
        	self.cache.move_to_end(key, last=False)
        	return self.cache[key]
        else:
        	return -1

    def set(self, key=None, value=None):
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

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.get(3))      # returns 3

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(4))          # returns -1 because cache was filled and overwritten

our_cache.set(-1,-1)             # Edge case
our_cache.set()                  # Edge case
our_cache.set(0,0)               # Edge case
our_cache.set(0.1,0.3)           # Edge case
our_cache.set("bob","bill")      # Edge case

print(our_cache.get(-1))         # return -1
print(our_cache.get())           # return None
print(our_cache.get(0))          # return 0
print(our_cache.get(0.1))        # return 0.3
print(our_cache.get("bob"))      # return "bill"