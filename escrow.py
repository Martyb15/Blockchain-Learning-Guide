import hashlib
import time
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Escrow: 
    id:               str
    sender:           str
    recipient:        str
    amount:           int
    secret_hash:      str
    created_at:       float
    timeout_blocks:   int
    status:           str = "pending"


class EscrowSystem: 
    def __init__(self): 
        self.escrow:         Dict[str, Escrow] = {}
        self.balances:       Dict[str, int]    = {}
        self.current_block = 0

    def set_balances(self, address: str, amount: int): 
        pass

    def get_balances(self) -> int:
        pass

    def create_escrow(self, sender: str, recipient:str, amount:int):
        pass

    def claim(self, escrow_id: str, secret: str, claimer: str):
        pass

    def refund(self, escrow_id: str) -> bool: 
        pass
    