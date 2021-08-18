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
        while current:
            s += str(current)
            s += "\n"
            current = current.next
        return s

ethereum = BlockChain()

for i in range(1,6):
    ethereum.add_block(i)
    time.sleep(0.01)

print(ethereum)