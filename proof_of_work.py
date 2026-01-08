# Make adding blocks cost something (prevents spam).
# Anyone could flood the network with blocks. Proof of Work solves this by requiring miners to solve a
# puzzle: find a number (nonce) that makes the block's hash start with a certain number of zeros.
import hashlib
import time

STAKE_REWARD_PERCENT = 0.02

class Block: 
    def __init__(self, data: str, previous_hash: str = "0"):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = None

    def compute_hash(self) -> str: 
        content = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()
    

    def mine(self, difficulty: int) -> dict: 
        # Keep guessing until hash starts with zeros
        target = "0" * difficulty
        attempts = 0
        start_time = time.time()

        while True: 
            self.hash = self.compute_hash() 
            attempts += 1

            if self.hash.startswith(target): 
                elapsed = time.time() - start_time
                return {"attempts": attempts, "time": elapsed, "nonce": self.nonce, "hash": self.hash}
            self.nonce += 1

        


if __name__ == "__main__":
    print("=== Proof of Work Demo ===")
    print("Mining blocks at different difficulties ")

    for difficulty in range(1,6): 
        block = Block("Test block at difficutly {difficulty}", "0")
        result = block.mine(difficulty)
        print()
        print(f"Difficulty {difficulty} (hash starts with {"0" * difficulty})")
        print(f"    Attempts: {result["attempts"]:,} ")
        print(f"    Time:     {result["time"]:.4f} seconds")
        print(f"    Nonce:    {result["nonce"]}")
        print(f"    Hash:     {result["hash"][:32]}...")

        print(f"Notice that each added zero roughly 16x the work!")

"""
Take-Home Challenge

Difficulty Analyzer
1. Plot mining time vs difficulty (1-6). What's the pattern?
2. Calculate your computer's hash rate (hashes per second).
3. Implement dynamic difficulty: if blocks mine too fast, increase difficulty.
4. BONUS: Add a mining progress indicator that prints every 100,000 attempts.
"""