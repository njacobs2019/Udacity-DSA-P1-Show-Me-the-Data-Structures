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

items = [1, 2, None, "five", 6.0, (1,2), [1,2,3]]

for i in items:
    ethereum.add_block(i)
    time.sleep(0.01)

print(ethereum)

# Timestamp: 2021-08-18_165101.978344
# Data: 1
# Hash:  a068ef1f7c1fdf84b2297c98d35be0b19252a0bbdc3adb50d9d25389781c7ee1
# Previous hash:  0

# Timestamp: 2021-08-18_165102.001775
# Data: 2
# Hash:  24463d682c4e5f27ab1e11533aab8374be80b395ca14f67877022ee174a469e6
# Previous hash:  a068ef1f7c1fdf84b2297c98d35be0b19252a0bbdc3adb50d9d25389781c7ee1

# Timestamp: 2021-08-18_165102.017602
# Data: None
# Hash:  10e06bcb96328c6d5d20c2a6a33a3e04999e5455f1880e17091e557e72f10eec
# Previous hash:  24463d682c4e5f27ab1e11533aab8374be80b395ca14f67877022ee174a469e6

# Timestamp: 2021-08-18_165102.032722
# Data: five
# Hash:  348ec98f72928da940ea916e0bb71687ba26aca8ca72809feb6daa418758c738
# Previous hash:  10e06bcb96328c6d5d20c2a6a33a3e04999e5455f1880e17091e557e72f10eec

# Timestamp: 2021-08-18_165102.048153
# Data: 6.0
# Hash:  8c9963820575a8ee6fe5208c288ad32355ce9f026338a96fd03f8973966e7d53
# Previous hash:  348ec98f72928da940ea916e0bb71687ba26aca8ca72809feb6daa418758c738

# Timestamp: 2021-08-18_165102.063453
# Data: (1, 2)
# Hash:  36308acd3dd94bb4018c80591a737ef90f5a5f1c28b89fe00c562978f3186322
# Previous hash:  8c9963820575a8ee6fe5208c288ad32355ce9f026338a96fd03f8973966e7d53

# Timestamp: 2021-08-18_165102.078202
# Data: [1, 2, 3]
# Hash:  d3f3982ded4405c1a56afc25f1ee2705ff869fada3b9642794141ed9cf9c2e8b
# Previous hash:  36308acd3dd94bb4018c80591a737ef90f5a5f1c28b89fe00c562978f3186322