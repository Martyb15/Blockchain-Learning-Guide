# A blockchain is also a state machine. We need to track balances and reject transactions from people who do not have enough funds. 
import hashlib
import time
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Transaction:
    sender:     str
    recipient:  str
    amount:     int

class Block: 
    def __init__(self, transactions: List[Transaction], previous_hash: str = "0"): 
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

        def compute_hash(self) -> str: 
            tx_str = "".join(f"{t.sender}{t.recipient}{t.amount}" for t in self.transactions)
            content = f"{self.timestamp}{tx_str}{self.previous_hash}"
            return hashlib.sha256(content.encode()).hexdigest()

class SimpleChain: 
    def __init__(self):
        self.chain = []
        self.pending: List[Transaction] = []
        self.balances = {}
        self._create_genesis()

    def _create_genesis(self): 
        genesis = Block([], "0")
        self.chain.append(genesis)

    def set_balance(self, address: str, amount: int):
        self.balances [address] = amount

    def get_balance(self, address: str) -> int: 
        return self.balances.get(address, 0)

    def add_transaction(self, tx: Transaction) -> bool:
        # check if sender has enought funds
        if tx.sender != "SYSTEM": 
            if self.get_balance(tx.sender, 0) < tx.amount:
                print(f"Rejected: {tx.sender} is broke!")
                return False
            #move money
            self.pending.append(tx)
            print(f"ACCEPTED: {tx.sender} -> {tx.recipient}: {tx.amount}")
            return True
    
    def mine_block(self) -> Block: 
        """Process all pending transactions into a new block."""
        if not self.pending: 
            print("Nothing to mine!")
            return None
        
        # Apply all transactions to balances
        for tx in self.pending: 
            if tx.sender != "SYSTEM": 
                self.balances[tx.sender] -= tx.amount
            self.balances[tx.recipient] = self.get_balance(tx.recipient) + tx.amount

        # Create the block
        block = Block(self.pending.copy(), self.chain[-1].hash)
        self.chain.append(block)
        self.pending.clear()

        print(f"MINED: Block {len(self.chain) - 1} with {len(block.transactions)}")
        return block


if __name__ == '__main__':
    bc = SimpleChain()

    # Give Alice starting funds
    bc.set_balance("Alice", 100)
    print(f"Initial: Alice has {bc.get_balance('Alice')}")
    print()

    # Valid transaction
    bc.add_transaction(Transaction("Alice", "Bob", 30))

    # Valid transaction
    bc.add_transaction(Transaction("Alice", "Candice", 20))

    # Invalid transaction (now that Alice's funds have been exhausted)
    bc.add_transaction(Transaction("Alice", "Dave", 200))
    print()

    # check final balances
    for name in ["Alice", "Bob", "Candice", "Dave"]:         # users are not properly tracked or stored yet (names are used as addresses here)
        bc.get_balance(f"{name}: {bc.get_balance(name)}")






    

""""
Take-Home Challenge

Build a Mini Bank
1. Add a get_balance(address) method that returns 0 for unknown addresses.
2. Implement fees: subtract (amount + fee) from sender, give fee to a 'MINER' address.
3. Add a transfer(sender, recipient, amount) method that creates and processes a transaction in one call.
4. BONUS: Prevent negative balances AND prevent overflow (numbers too large).
"""