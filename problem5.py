import hashlib
from datetime import datetime
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = None
        self.data = data
        self.previous_hash = previous_hash
        self.hash = None
        self.next=None

        self.set_time()
        self.calc_hash()

    def set_time(self):
        now = now = str(datetime.now())
        now = now.replace(" ","_")
        now = now.replace(":","")
        self.timestamp = now

    def calc_hash(self):
        sha = hashlib.sha256()

        s=""
        s+="Timestamp: {}\n".format(self.timestamp)
        s+="Data: {}\n".format(self.data)
        s+="Previous hash:  {}\n".format(self.previous_hash)

        hash_str = s.encode('utf-8')
        sha.update(hash_str)
        self.hash = sha.hexdigest()

    def __repr__(self):
        s=""
        s+="Timestamp: {}\n".format(self.timestamp)
        s+="Data: {}\n".format(self.data)
        s+="Hash:  {}\n".format(self.hash)
        s+="Previous hash:  {}\n".format(self.previous_hash)
        return s

class BlockChain:
    def __init__(self):
        self.genesis = None
        self.tail = None
        self.length = 0

    def add_block(self,data):
        time.sleep(0.01)
        # Case we are adding the first block
        if self.genesis==None:
            new_block = Block(data,0)
            self.genesis = new_block
            self.tail = new_block

        # Case we are adding a block that isn't the first
        else:
            previous_hash = self.tail.hash
            self.tail.next = Block(data, previous_hash)
            self.tail = self.tail.next

        self.length += 1

    def __repr__(self):
        s=""
        current = self.genesis

        if current is None:
            s+="<empty>\n"

        while current:
            s += str(current)
            s += "\n"
            current = current.next
        return s


if __name__=='__main__':

    # Test Case 1:  Standard use with many different types of data in the blocks
    b1 = BlockChain()
    print("\nFirst test case:")

    items = [1, 2, None, "five", 6.0, (1,2), [1,2,3]]
    for i in items:
        b1.add_block(i)

    print(b1)

    # Output:
    # First test case:
    # Timestamp: 2021-08-19_223553.648985
    # Data: 1
    # Hash:  d2888f0ce210c17e6bed160d7ad6c957cc3f1d4b5a48a7d8808bd2b752d70b0a
    # Previous hash:  0

    # Timestamp: 2021-08-19_223553.659631
    # Data: 2
    # Hash:  48f16e648f35546b54c41d561c98de3ebac3bef0eda709a27696dbb84764ab0d
    # Previous hash:  d2888f0ce210c17e6bed160d7ad6c957cc3f1d4b5a48a7d8808bd2b752d70b0a

    # Timestamp: 2021-08-19_223553.670256
    # Data: None
    # Hash:  8793f098860f334d76c3e7a2f3f1c0ec4e801a5f1cd296c1d2cc719d64961e71
    # Previous hash:  48f16e648f35546b54c41d561c98de3ebac3bef0eda709a27696dbb84764ab0d

    # Timestamp: 2021-08-19_223553.680885
    # Data: five
    # Hash:  babb53239b9cdd1a0119c27f7b856c9195753bdb68ed6ec75173ec0407659a0e
    # Previous hash:  8793f098860f334d76c3e7a2f3f1c0ec4e801a5f1cd296c1d2cc719d64961e71

    # Timestamp: 2021-08-19_223553.691615
    # Data: 6.0
    # Hash:  b4da39a8036e18c5e4c54f8fde98dfd4fbf2688cfd7bfa7e287e2c9d34226c8f
    # Previous hash:  babb53239b9cdd1a0119c27f7b856c9195753bdb68ed6ec75173ec0407659a0e

    # Timestamp: 2021-08-19_223553.702225
    # Data: (1, 2)
    # Hash:  b18aac19e4904d51504f781faf9456463a021453138debd77b8ff1366f228bc9
    # Previous hash:  b4da39a8036e18c5e4c54f8fde98dfd4fbf2688cfd7bfa7e287e2c9d34226c8f

    # Timestamp: 2021-08-19_223553.713140
    # Data: [1, 2, 3]
    # Hash:  2b1e2d4cf1dbc286ead17b3d808cd27bda62d86fd4722bb0d9d8401b951c260d
    # Previous hash:  b18aac19e4904d51504f781faf9456463a021453138debd77b8ff1366f228bc9



    # Test Case 2:  Empty chain
    b2 = BlockChain()
    print("\nSecond test case:")
    print(b2)

    # Output:
    # <empty>

    # Test Case 3:  Trying to add blocks sequentially to get same time
    b3 = BlockChain()
    print("\nThird test case:")
    
    items = [1, 2, 3]
    for i in items:
        b3.add_block(i)

    print(b3)

    # Output:
    # Timestamp: 2021-08-19_223553.723594
    # Data: 1
    # Hash:  15e34a9f1c261c33f3655902a0b935b1d827ebfa10ffb29051d7edc9a8eb785f
    # Previous hash:  0

    # Timestamp: 2021-08-19_223553.734276
    # Data: 2
    # Hash:  a8a52ac0e028107620262f08f0fc36c9858ad77c35458d98e4dbd036b61ec7be
    # Previous hash:  15e34a9f1c261c33f3655902a0b935b1d827ebfa10ffb29051d7edc9a8eb785f

    # Timestamp: 2021-08-19_223553.744950
    # Data: 3
    # Hash:  1912c821d7c650eba52457e2d7c909a5855e1d8a364b641333c97b4e424324cb
    # Previous hash:  a8a52ac0e028107620262f08f0fc36c9858ad77c35458d98e4dbd036b61ec7be
