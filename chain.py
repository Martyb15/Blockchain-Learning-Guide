import hashlib
import time 

class Block: 
    def __init__(self, data: str, prev_hash: str =''):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        content = f"{self.timestamp} {self.data} {self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

# Change block 1 → its hash changes → block 2's link breaks
chain = []
chain.append(Block('gensis block', 0))
chain.append(Block('Alice Pays Bob 50', chain[-1].hash))
chain.append(Block('Bob pays Charlie 25', chain[-1].hash))

for i, block in enumerate(chain): 
    print(f"Block {i}: {block.data[:20]}... -> {block.hash[:16]}...")

"""
Take-Home Challenge
Visualize the Chain
1. Write a function print_chain(chain) that displays the chain visually, showing how each block's
previous_hash matches the prior block's hash.
2. Build a chain of 10 blocks. Now change block #3's data. Print the chain and show which links are now
broken.
3. BONUS: Create an add_block(chain, data) function that automatically links to the last block.

"""