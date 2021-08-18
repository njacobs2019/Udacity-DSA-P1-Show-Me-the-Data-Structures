import sys
from collections import deque

class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Node:  
    def __init__(self,huffnode = None):
        self.huffnode = huffnode
        self.left = None
        self.right = None
        
    def set_huffnode(self,huffnode):
        self.huffnode = huffnode
        
    def get_value(self):
        return str(self.huffnode.char)+str(self.huffnode.count)

    def get_char(self):
        return self.huffnode.char

    def get_count(self):
        return self.huffnode.count
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
class HuffNode(Node):
    def __init__(self, count=None, char=None):
        super().__init__()
        self.count=count
        self.char=char
    
    def get_value(self):
        return str(self.char)+str(self.count)
    
    def set_huffnode(self):
        raise RuntimeError
    
class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,node):
        self.root = node
        
    def get_root(self):
        return self.root
    
    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_count() == node.get_count():
            if new_node.get_char()==None or node.get_char()==None:
                return -1
            elif ord(new_node.get_char()) < ord(node.get_char()):
                return -1
            else:
                return 1
        elif new_node.get_count() < node.get_count():
            return -1
        else:
            return 1
    
    def insert(self,new_node):
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping
    def pop_min_node(self):
        current = self.get_root()
        # Case: No left child
        if not current.has_left_child():
            temp = current
            self.set_root(current.get_right_child())
            return temp

        # Case: Has a left child
        else:
            while current.left.left is not None:
                current=current.left
            temp=current.left
            current.left=current.left.right
            return temp
    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "\nTree"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level
        return s

class HuffTree(Tree):
    def __init__(self, root):
        super().__init__()
        self.root = root

def calc_frequencies(data):
    freqencies = {}

    for element in data:
        if element in freqencies:
            freqencies[element]+=1
        else:
            freqencies[element]=1
    return freqencies

def gen_forward_map(root):
    return _gen_forward_map(root, {}, "")

def _gen_forward_map(root, mapping, sequence):
    # If move right
    if root.left:
        left_sequence = sequence+"0"
        mapping = _gen_forward_map(root.left, mapping, left_sequence)
    
    if root.right:
        right_sequence = sequence+"1"
        mapping = _gen_forward_map(root.right, mapping, right_sequence)
    
    mapping[root.char]=sequence
    return mapping

def huffman_encoding(data):
    frequencies = calc_frequencies(data)
    tree = Tree()

    # Fill the tree with nodes pointing to huffnodes
    for key, value in frequencies.items():
        temp_huff = HuffNode(count=value, char=key)
        temp_node = Node(huffnode=temp_huff)
        tree.insert(temp_node)

    # Links the huffnodes
    while tree.get_root().has_left_child() or tree.get_root().has_right_child():
        smallest = tree.pop_min_node().huffnode
        next_smallest = tree.pop_min_node().huffnode
        count = smallest.count+next_smallest.count
        new_huff = HuffNode(count=count)
        new_huff.left=smallest
        new_huff.right=next_smallest
        temp = Node(new_huff)
        tree.insert(temp)

    # Find mapping
    huff_root = tree.get_root().huffnode
    mapping = gen_forward_map(huff_root)

    # Compress the data
    encoded = ""
    for char in data:
        encoded = encoded + mapping[char]

    return encoded, huff_root

def huffman_decoding(data,root):
    data = str(data)
    decoded = ""
    current = root

    for bit in data:
        if bit=='0':
            current = current.left
        else:
            current = current.right


        # Case when at leaf node
        if current.char:
            decoded += current.char
            current=root


    return decoded

# if __name__ == '__main__':
#     data = "TheBirdIsTheWord"
#     print("Input: {}".format(data))

#     compressed, root = huffman_encoding(data)

#     print("Compressed: {}".format(compressed))

#     huff_tree = HuffTree(root)
#     print(huff_tree)

#     decoded = huffman_decoding(compressed, root)

#     print("\nDecoded: {}".format(decoded))


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))