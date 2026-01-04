# Make adding blocks cost something (prevents spam).
# Anyone could flood the network with blocks. Proof of Work solves this by requiring miners to solve a
# puzzle: find a number (nonce) that makes the block's hash start with a certain number of zeros.
from transactions import Transaction

DIFFUCULTY = 4

# class Block:
#     def __init__(self, data: str):
#         self.timestamp = time.time()
#         self.data      = data 
#         self.hash      = self.compute_hash()

#     def compute_hash(self) -> str:
#         content = f"{self.timestamp} {self.data}"
#         return hashlib.sha256(content.encode()).hexdigest()

class Block: 
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = None

    def mine(self): 
        # Keep guessing until hash starts with zeros
        target = "0" * DIFFUCULTY 
    

        while True: 
            test_hash = self.compute_hash()
            if test_hash.startswith(target): 
                self.hash = test_hash
                print(f"Found! Nonce = {self.nonce}")
                print(f"Hash = {self.hash[:20]}]")
                return
            self.nonce += 1


if __name__ == "__main__":
    tx1 = Transaction("Alice", "Bob", 50)
    block = Block([tx1], 0)
    block.mine()
