import hashlib
import time

class Block: 
    def __init__(self, data: str, previous_hash: str = '0'):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        content = f"{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

def build_chain(data_list: list) -> list:
    chain = []
    previous_hash = "0"
    for data in data_list:
        block = Block(data, previous_hash)
        chain.append(block)
        previous_hash = block.hash
    return chain

def is_chain_valid(chain: list[Block]) -> bool:
    """Check if the entire chain is valid (untampered)"""
    for i in range(1, len(chain)): 
        current = chain[i]
        previous = chain[i - 1]

    # Check 1: Has this blocked been tampered with? 
        if current.hash != current.compute_hash(): 
            print(f"Block {i} has been modified")
            return False
    # Check 2: Is the link to previous block intact? 
        if current.previous_hash != previous.hash: 
            print(f"Block {i} link is broken!")
            return False
    print(f"VALID: Chain integrity verified!")
    return True


if __name__ == "__main__":
    chain = build_chain([
        "Genesis Block",
        "Alice pays Bob 50",
        "Bob pays Carol 25",
    ])
    print("=== Testing Valid Chain ===")
    pass
    print("=== Tampering With Block 1 ===")
    pass
    print("=== Attacker Tries to Fix Hash ===")


"""
Take-Home Challenge

The Attacker Simulation
1. Write a function tamper_block(chain, index, new_data) that changes a block's data and tries to "fix" the
chain by recalculating hashes.
2. Can you make the tampered chain pass validation? What would you need to recalculate?
3. BONUS: Create a detailed_validation(chain) function that returns a report of ALL problems found, not
just the first one.
"""