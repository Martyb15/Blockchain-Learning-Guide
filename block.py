import hashlib
import time


# A block is just data + metadata + fingerprint
# The hash "seals" the contents — any change is detectable
class Block:
    def __init__(self, data: str):
        self.timestamp = time.time()
        self.data      = data 
        self.hash      = self.compute_hash()

    def compute_hash(self) -> str:
        content = f"{self.timestamp} {self.data}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    
block = Block("Alice pays Bob 50")
print(f"Data : {block.data}")
print(f"Hash : {block.hash}")


"""
Take-Home Challenge

Build a Better Block
1. Add a 'creator' field to the Block class that stores who created it. Update compute_hash to include this
field.
2. Create a method called is_tampered() that returns True if someone changed the data after creation.
3. BONUS: Add a __str__ method that prints the block nicely formatted.
"""