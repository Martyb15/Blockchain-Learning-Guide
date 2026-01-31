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



def is_chain_valid(chain: list[Block]) -> bool:
    for i in range(1, len(chain)): 
        current = chain[i]
        previous = chain[i - 1]

        if current.hash != current.compute_hash(): 
            print(f"Block {i} has been modified")
            return False
        
        if current.previous_hash != previous.hash: 
            print(f"Block {i} link is broken!")
            return False
        
    return True

print(is_chain_valid(chain))
chain.data[1] = "Alice pays Bob 999999"
print(is_chain_valid(chain))


"""
Take-Home Challenge

The Attacker Simulation
1. Write a function tamper_block(chain, index, new_data) that changes a block's data and tries to "fix" the
chain by recalculating hashes.
2. Can you make the tampered chain pass validation? What would you need to recalculate?
3. BONUS: Create a detailed_validation(chain) function that returns a report of ALL problems found, not
just the first one.
"""