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
    
    if len(sequence)==0:
        sequence = sequence+"0"
    mapping[root.char]=sequence
    return mapping

def huffman_encoding(data):
    if not isinstance(data, str):
        data = str(data)
        print("Warning:  data to be encoded was converted to a string")

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
        if not current.char:
            if bit=='0':
                current = current.left
            else:
                current = current.right

        # Case when at leaf node
        if current.char:
            decoded += current.char
            current=root

    return decoded


if __name__ == "__main__":
    
    sentences = []
    sentences.append("The bird is the word")
    sentences.append("Sebastian Thrun (born May 14, 1967) is an entrepreneur, educator, and computer scientist from Germany. He is CEO of Kitty Hawk Corporation, and chairman and co-founder of Udacity. Before that, he was a Google VP and Fellow, a Professor of Computer Science at Stanford University, and before that at Carnegie Mellon University. At Google, he founded Google X and Google's self-driving car team. He is also an Adjunct Professor at Stanford University and at Georgia Tech.[4]")
    sentences.append("Hello")
    sentences.append("!?")
    sentences.append("54")
    sentences.append("AAAAAAAA")
    sentences.append(5)
    sentences.append(None)

    for sentence in sentences:
        print("--"*10)
        print ("The size of the data is: {}".format(sys.getsizeof(sentence)))
        print ("The content of the data is: {}\n".format(sentence))
        
        encoded_data, tree = huffman_encoding(sentence)
        print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

# Output of testing:
# --------------------
# The size of the data is: 69
# The content of the data is: The bird is the word

# The size of the encoded data is: 36
# The content of the encoded data is: 1100001101010110010000011101100001111110111000110101011101111100011101

# The size of the decoded data is: 69
# The content of the encoded data is: The bird is the word

# --------------------
# The size of the data is: 521
# The content of the data is: Sebastian Thrun (born May 14, 1967) is an entrepreneur, educator, and computer scientist from Germany. He is CEO of Kitty Hawk Corporation, and chairman and co-founder of Udacity. Before that, he was a Google VP and Fellow, a Professor of Computer Science at Stanford University, and before that at Carnegie Mellon University. At Google, he founded Google X and Google's self-driving car team. He is also an Adjunct Professor at Stanford University and at Georgia Tech.[4]

# The size of the encoded data is: 320
# The content of the encoded data is: 10011110001101111011001101001010010110010001111010111001110001101010101000111100101001110111101011011010001110111100111000111011110111101001111011011111111011110101001011011001011111001011001001011101110010110101111100100011100010000101011000010011010110000100000010101001100111111110001010010101000110110001011011011001111111111001000101001110011010110100001001101101010010100001101111101000110001000010000101001011010010111101001011010110100001110011110000110010000110010000111011101110111001110000011100101101011110011101001000111001001101111011010011111001000010010010101010111011110011100110011011111101011110111100111010110110100110110110110110001010010101110000111111111100100010100111001100111001100001001100100001100100011111001000101001110011010111001010101001101110101010001010000001101111011010011111001100101001100001100010010101110111011101111001000100000100110110110000111010101110011000101011111111011100000111110111111100110101111100111001111101110110100011101100001111001001110011101111110010001010011110010000000011011011011010111101111101111111111001110011101011010110100100011010110101011011011110110100111110011101011010000100110110101001010000110111100111100110001000010000011000011111000101111100111101011100100001001101101101010011110011001000001010101100000110110100010010101110101111111111001000101001111101111000001001101101100001110101011100110001011111100010111110011101100011010000000100010010000111011110010001101101101101011100011110011001000001010101100000110110100010010101110111011101110111100001011110011111011101101000111011000001111111101110000011101001101110101010001010000010100111001111101110110100011101100001111001001001111100100010100111001111101110110100011101100001001010001101011111010000110110010011001010110100011000101010110001010000100011110011011000110111010100011000100001101110111001110000011100101101011111001101101101010111111100100011101111000101001010111111101010100000110010111100111010110101101001000110101101010110110111110001011111001111010111001000010011011011010100111100110010000010101011000001101101000100101011101111110010001010011111000101111001111000101101100100010010110011110101110000001100111001101110100100101011110111010111110

# The size of the decoded data is: 521
# The content of the encoded data is: Sebastian Thrun (born May 14, 1967) is an entrepreneur, educator, and computer scientist from Germany. He is CEO of Kitty Hawk Corporation, and chairman and co-founder of Udacity. Before that, he was a Google VP and Fellow, a Professor of Computer Science at Stanford University, and before that at Carnegie Mellon University. At Google, he founded Google X and Google's self-driving car team. He is also an Adjunct Professor at Stanford University and at Georgia Tech.[4]

# --------------------
# The size of the data is: 54
# The content of the data is: Hello

# The size of the encoded data is: 28
# The content of the encoded data is: 1101110010

# The size of the decoded data is: 54
# The content of the encoded data is: Hello

# --------------------
# The size of the data is: 51
# The content of the data is: !?

# The size of the encoded data is: 28
# The content of the encoded data is: 01

# The size of the decoded data is: 51
# The content of the encoded data is: !?

# --------------------
# The size of the data is: 51
# The content of the data is: 54

# The size of the encoded data is: 28
# The content of the encoded data is: 10

# The size of the decoded data is: 51
# The content of the encoded data is: 54

# --------------------
# The size of the data is: 57
# The content of the data is: AAAAAAAA

# The size of the encoded data is: 24
# The content of the encoded data is: 00000000

# The size of the decoded data is: 57
# The content of the encoded data is: AAAAAAAA

# --------------------
# The size of the data is: 28
# The content of the data is: 5

# Warning:  data to be encoded was converted to a string
# The size of the encoded data is: 24
# The content of the encoded data is: 0

# The size of the decoded data is: 50
# The content of the encoded data is: 5

# --------------------
# The size of the data is: 16
# The content of the data is: None

# Warning:  data to be encoded was converted to a string
# The size of the encoded data is: 28
# The content of the encoded data is: 10010011

# The size of the decoded data is: 53
# The content of the encoded data is: None
