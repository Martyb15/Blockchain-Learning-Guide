from dataclasses import dataclass
from typing import List
import time
import hashlib

# Transactions are the "content" of blocks
# Structure makes validation easier

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
        # Include all transaction data in the hash
        tx_data = "".join(str(tx) for tx in self.transactions)
        content = f"{self.timestamp}{tx_data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

    def total_value(self) -> int:
        """Sum of all transaction amounts in this block."""
        return sum(tx.amount for tx in self.transactions)


# === RUN THE DEMO ===
if __name__ == "__main__":
    # Create some transactions
    tx1 = Transaction("Alice", "Bob", 50)
    tx2 = Transaction("Bob", "Carol", 25)
    tx3 = Transaction("Carol", "Dave", 10)
    print("=== Individual Transactions ===")
    print(tx1)
    print(tx2)
    print(tx3)
    print()
    # Create a block with multiple transactions
    block = Block([tx1, tx2, tx3], "0")
    print("=== Block Info ===")
    print(f"Number of transactions: {len(block.transactions)}")
    print(f"Total value moved: {block.total_value()}")
    print(f"Block hash: {block.hash[:32]}...")
    print()
    # Show all transactions in the block
    print("=== Transactions in Block ===")
    for i, tx in enumerate(block.transactions):
        print(f" {i+1}. {tx}")

"""
Take-Home Challenge

Transaction Types
1. Add a 'fee' field to Transaction. Modify total_value() to include fees.
2. Add a 'timestamp' field that records when each transaction was created.
3. Add a tx_type field ('PAY', 'REWARD', 'FEE'). Filter transactions by type.
4. BONUS: Add a unique transaction ID (hash of sender+recipient+amount+timestamp).
"""