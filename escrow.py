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
        self.escrows:         Dict[str, Escrow] = {}
        self.balances:       Dict[str, int]    = {}
        self.current_block = 0

    def set_balances(self, address: str, amount: int): 
        self.balances[address] = amount

    def get_balances(self, address: str) -> int:
        return self.balances.get(address, 0)

    def create_escrow(self, sender: str, recipient:str, amount:int, secret_hash: str, timeout_blocks: int = 10) -> Optional[str]:
        if self.get_balance(sender) < amount:
            print(f"FAILURE: {sender} has insufficient funds")
            return None
        escrow_id = hashlib.sha256(f"{sender}{recipient}{amount}{time.time()}".encode).hexdigest()[:16]
        self.balances[sender] -= amount 
        self.escrows[escrow_id] = Escrow(
            id = escrow_id,
            sender = sender,
            recipient = recipient, 
            amount = amount, 
            secret_hash = secret_hash,
            created_at = self.current_block,
            timeout_blocks = timeout_blocks
            )
        print(f"ESCROW CREATED: {escrow_id}")
        return escrow_id

    def claim(self, escrow_id: str, secret: str, claimer: str):
        pass

    def refund(self, escrow_id: str) -> bool: 
        pass
