from dataclasses import dataclass
from typing import List

# Transactions are the "content" of blocks
# Structure makes validation easier

@dataclass
class Transaction: 
    sender:     str
    recipient:  str
    amount:     int

@dataclass 
class Block:
    transactions: List[Transaction]
    previous_hash: str
    timestamp: float = None
    hash: str = None


if __name__ == '__main__':
    block = Block()

    tx1 = Transaction("Alice", "Bob", 50)
    tx2 = Transaction("Bob", "Carol", 25)

    print(f"Block contains {len(block.transactions)} transactions")
    print(f"First tx {tx1.sender} -> {tx1.recipient}: {tx1.amount}")


"""
Take-Home Challenge

Transaction Types
1. Add a 'fee' field to the Transaction class. Fees go to whoever processes the transaction.
2. Add a 'timestamp' field that records when the transaction was created.
3. Create a method total_value() on Block that returns the sum of all transaction amounts.
4. BONUS: Add a tx_type field with values like 'PAY', 'REWARD', 'FEE'. How might you use this?
"""