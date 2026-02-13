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
    
def build_chain(data_list: list) -> list: 
    """ Build a chain of blocks from a list of data strings """
    chain = []
    previous_hash = "0"    # Genesis block has no previous

    for data in data_list: 
        block = Block(data, previous_hash)
        chain.append(block)
        previous_hash = block.hash     # next block will point to this one

    return chain


def print_chain(chain: list ): 
    """ Visualize the chain showing links """
    print("=" * 60)
    for i, block in enumerate(chain):
        print(f"Block {i}:")
        print(f" Data: {block.data}")
        print(f" Previous: {block.previous_hash[:16]}...")
        print(f" Hash: {block.hash[:16]}...")
        if i < len(chain) - 1:
            print(" |")
            print(" v")
    print("=" * 60)

# === RUN THE DEMO ===
if __name__ == "__main__":
# Build a chain of transactions
    transactions = [
    "Genesis Block",
    "Alice pays Bob 50",
    "Bob pays Carol 25",
    "Carol pays Dave 10"
    ]
    chain = build_chain(transactions)
    print_chain(chain)
    # Show the linking
    print("\n=== Verify Links ===")
    for i in range(1, len(chain)):
        prev_hash = chain[i-1].hash
        stored_prev = chain[i].previous_hash
        matches = prev_hash == stored_prev
        print(f"Block {i} points to Block {i-1}: {matches}")
"""
Take-Home Challenge
Visualize the Chain
1. Build a chain of 10 blocks. Change block #3's data. Show which links break.
2. Create an add_block(chain, data) function that automatically links to the last block.
3. BONUS: Create an ASCII art visualization showing blocks as boxes connected by arrows.

"""