# Why would anyone spend electricity mining? Because they get paid! Each block includes a special
# "coinbase" transaction that creates new coins and gives them to the miner.
import hashlib
import time
from dataclasses import dataclass
from typing import List, Dict

BLOCK_REWARD = 50
DIFFICULTY = 4

@dataclass
class Transaction: 
    sender:    str
    recipient: str
    amount:    int
    fee:       int = 0

class Block:
    def __init__(self, transactions: List[Transaction], previous_hash: str):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = ""

    def compute_hash(self) -> str:
        tx_str = "".join(f"{t.sender}{t.recipient}{t.amount}" for t in self.transactions)
        content = f"{self.timestamp}{tx_str}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def mine(self, difficutly: int): 
        target = "0" * difficutly
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()


class Blockchain:
    def __init__(self):
        self.chain = List[Block] = []
        self.pending = List[Transaction] = []
        self.balances = Dict[str, int] = {}
        genesis = Block([], "0")
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)

    def add_transaction(self, tx: Transaction) -> bool: 
        if tx.sender != "SYSTEM": 
            if self.balances.get(tx.sender, 0) < (tx.amount + tx.fee): 
                return False
        self.pending.append(tx)
        return True

    def mine_block(self, miner_address: str) -> Block:
        total_fees = sum(tx.fee for tx in self.pending)
        reward = BLOCK_REWARD + total_fees
        system_tx = Transaction("SYSTEM", miner_address, reward)
        all_txs = [system_tx] + self.pending.copy()


        block = Block(all_txs, self.chain[-1].hash)
        print(f"Mining block {len(self.chain)}...", end="  ")
        block.mine(DIFFICULTY)

        for tx in all_txs:
            if tx.sender != "SYSTEM":
                self.balances[tx.sender] -= (tx.amount + tx.fee)
            self.balances[tx.recipient] = self.balances.get(tx.recipient, 0) + tx.amount

        self.chain.append(block)
        self.pending.clear()
        return block
    
# ==== Running the Demo ====
if __name__ == "__main__": 
    bc = Blockchain
    bc.balances["Alice", 0] = 100 

    print("Mining Reward Demo")
    bc.add_transaction(Transaction("Alice", "Bob", 30, fee=5))
    bc.mine_block("Miner1")

    print(f"\nBalances after Block 1")
    print(f"Alice:     {bc.balances.get("Alice", 0)} (paid 30 + 5 fee)")
    print(f"Bob:       {bc.balances.get("Blob", 0)} (recieved 30)")
    print(f"Miner1:    {bc.balances.get("Miner1", 0)} (reward {BLOCK_REWARD} + 5 fee)")



"""
Take-Home Challenge

Bitcoin Economics
1. Implement halving: cut reward in half every 10 blocks.
2. Add get_total_supply() to count all coins ever created.
3. Calculate: with halving every 10 blocks, what's the max supply?
4. BONUS: Prioritize transactions by fee (highest fee first).




What you learn:
• New coins are created as mining rewards
• This is how Bitcoin/Ethereum create new currency
• Miners compete because they want the reward
"""
