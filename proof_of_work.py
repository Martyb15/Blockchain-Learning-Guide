# Make adding blocks cost something (prevents spam).
# Anyone could flood the network with blocks. Proof of Work solves this by requiring miners to solve a
# puzzle: find a number (nonce) that makes the block's hash start with a certain number of zeros.
import random
from transactions import Transaction
from dataclasses import dataclass
from typing import Dict

STAKE_REWARD_PERCENT = 0.02

@dataclass
class Validator: 
    address: str
    stake: int
    blocks_created: int = 0

class ProofOfStake: 
    def __init__(self): 
        self.validators: Dict[str, Validator] = {}
        self.balances: Dict[str, int] = {}


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


"""
Take-Home Challenge

Staking Simulator
1. Run 1000 selections. Does each validator's win rate match their stake %?
2. Add a minimum stake requirement (e.g., 100 coins).
3. Implement an unstaking delay (can't unstake for 10 blocks).
4. BONUS: Auto-detect double-signing and slash automatically.
"""