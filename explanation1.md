The OrderedDict was chosen to hold the cache for both simplicity and time+space complexities.  It can be easily imported from the collections library built into Python.  It implements a doubly-linked list and hashmap in the background to allow for fast, O(1) data writting and retreival because of the hashmap and fast reordering of elements to record which is the least recently used by means of the doubly-linked list.  Adding and accessing data both have O(1) worst-case time complexities.  The algorithm has a space complexity of O(n).  This is the theoretical limit for space complexity as at least one copy of element needs to be retained.