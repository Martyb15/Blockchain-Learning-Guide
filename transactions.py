from dataclasses import dataclass
from typing import List

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
    