Union Analysis:
A set of llist_1 is first created because sets remove duplicate elements and have constant time insertion, deletion, and checking if an element exists.  This takes O(n) time as llist_1 has to be traversed.  All values in llist_2 are next added to the set.  This ensures that there are no duplicates and takes O(n) time.  Finally, the set is traversed to create a linked list to output.  This all takes O(n) time and O(n) memory.

Intersection Analysis:
Two sets, for llist_1 and llist_2 are first created.  This takes O(n) time and O(n) memory.  Sets ensure that there are no duplicate elements in the output and allow for constant time checking if an element is contained within it.  The second set is now iterated over and if the element exists in the first set, the element is appended to the output linked list.  This takes O(n) time and O(n) memory.  For a total algorithmic time, complexity of O(n) and space complexity of O(n).
