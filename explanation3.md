Please note that the queue class and deque are implemented to traverse the trees for visualization/debugging purposes only.

Algorithm:
1. Character frequencies were stored in a dictionary because they allow for O(1) time insertions and accesses and O(n) space complexity.  As all elements of the input string needed to be traversed, this takes O(n) time.

Two trees were used to solve this problem.  A priority tree with standard nodes eventually becomes a standard node connected to the entire Huffman tree.  Each standard node connects to at least one Huffman node and potentially two other standard nodes.  The value of the standard node is the value of the attached Huffman node.  This priority tree is sorted in binary fashion with all left children being smaller than the parent and all right children larger.

2. The frequency dictionary is iterated over once.  Each element is turned into a Huffman node connected to a standard node and inserted onto the priority tree in sorted fashion.  Accessing a dictionary element and creating the new node takes O(1) time but adding it to the tree takes O(log(n)) time.  As this is done n times, the total time complexity for this operation is O(n*log(n)).  The space complexity of this operation is O(n).

3.  The Huffman nodes now need to be assembled into the Huffman tree.  The two smallest standard nodes are popped from the priority tree.  Their Huffman nodes are merged and connected to a new standard node which is re-inserted back into the tree until only one standard node is left.  Popping and inserting nodes takes O(log(n)) time.  As this is done at most n times, overall time complexity is O(n*log(n)).

4.  A dictionary of each character to its Huffman code is created by traversing the entire tree which takes O(n) time.  This dictionary is used to encode the original input data in O(n) time.

5.  The encoded message is decoded by traversing the Huffman tree for each encoded bit.  This takes a total of O(n*log(n)) time.

The time complexity of the algorithm is O(n*log(n)) while its space complexity is O(n).
