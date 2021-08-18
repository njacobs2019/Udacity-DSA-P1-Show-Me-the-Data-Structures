This problem was solved recursively for simplicity.  The file structure is analagous to a tree which needs to be traversed once.  To be traversed iteratively a stack would need to be explicitly created for DFS or a queue for a BFS.  The recursive implementation does implement a stack, but it is created behind the scenes by the Python interpreter as the call stack with each recursive call.  As this algorithm needs to look at all files, subfiles, and directories, its time complexity is O(n) which is best case for this problem as the data is unordered.  The space complexity is at worst O(n) because there can be at most n items returned in the list if all items are of the given extension.