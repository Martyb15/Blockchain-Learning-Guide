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
        """
        Create a fingerprint of this block's contents.
        
        :param self: Description
        :return: Description
        :rtype: str
        """
        content = f"{self.timestamp} {self.data}"
        return hashlib.sha256(content.encode()).hexdigest()

    def __str__(self): 
        return f"Block(data= '{self.data[:30]}...', hash={self.hash[:16]}...)"
    
if __name__ == "__main__":

    block = Block("Alice pays Bob 50 coins")

    print("===== Block Created =====")
    print("=== Block Created ===")
    print(f"Data: {block.data}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Hash: {block.hash}")
    print()
    
    # Show that the hash "seals" the content
    print("=== Tampering Detection ===")
    original_hash = block.hash

    # Tamper with the data
    block.data = "Alice pays Bob 9999 coins"
    new_hash = block.compute_hash()
    print(f"Original hash: {original_hash[:32]}...")
    print(f"Hash after tampering:{new_hash[:32]}...")
    print(f"Hashes match: {original_hash == new_hash}")
    print()
    print("The hash changed because the data changed!")


"""
Take-Home Challenge

Build a Better Block
1. Add a 'creator' field to the Block class. Update compute_hash to include this field.
2. Create a method is_tampered() that returns True if the stored hash doesn't match a freshly computed
hash.
3. BONUS: Add a __repr__ method that shows all block fields in a nice format.
4. BONUS: Add a __str__ method that prints the block nicely formatted. [DONE]
"""