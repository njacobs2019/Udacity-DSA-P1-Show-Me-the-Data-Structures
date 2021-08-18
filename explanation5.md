A linked list was used to implement the blockchain as it allows for fast, O(1) appends.  For the test case, note that your output will slightly differ.  The timestamp will differ which will change the hash, but the hashes and previous hashes will still match.  The hash of a block depends on its timestamp, its data, and the previous hash.  The first block, or genesis block, has a previous hash of 0.  Adding a new block to the blockchain takes O(1) time, but traversing the blockchain to print everything takes O(n) time which is the best-case for this problem.  The space complexity of this algorithm is also O(n) which is the theoretical minimum as each block needs to be stored at least once.