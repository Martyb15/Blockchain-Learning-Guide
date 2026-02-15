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

    def set_balance(self, address: str, amount: int): 
        self.balances[address] = amount

    def get_balance(self, address: str) -> int:
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
       escrow = self.escrows.get(escrow_id)
       if not escrow or escrow.status != "pending": 
           return False
       if claimer != escrow.recipient: 
           print(f"FAILED: Only recipient can claim")
           return False
       if hashlib.sha256(secret.encode()).hexdigest() != escrow.secret_hash:
           print("FAILED: Wrong secret!")
           return False
       self.balances[escrow.recipient] = self.get_balance(escrow.recipient) + escrow.amount
       escrow.status = "claimed"
       print(f"CLAIMED: {escrow.recipient} recieve {escrow.amount}")
       return True 

    def refund(self, escrow_id: str) -> bool: 
        escrow = self.escrow.get(escrow_id)
        if not escrow or escrow.status !=  "pending": 
            return False
        if self.current_block < escrow.created_at + escrow.timeout_blocks: 
            print(f"FAILED: Escrow not expired yet")

    def advance_blocks(self, n: int = 1): 
        self.current_block += n
        print(f"Advanced to block {self.current_block}")


# ==== Run the Demo ====
if __name__ == "__main__": 
    system = EscrowSystem()
    system.set_balance("Alice", 100)

    secret = "mango123" 
    secret_hash = hashlib.sha256(secret.encode()).hexdigest()

    print("=== Creating Escrow ===")
    escrow_id = system.create_escrow("Alice", "Bob", 50, secret_hash, timeout_blocks=5)
    print("\n=== Bob Tries Wrong secret ===")
    system.claim(escrow_id, "wrong_guess", "Bob")

    print("\n=== Bob Uses Correct Secret ===")
    system.claim(escrow_id, secret, "Bob")
    print(f"Bob's balance: {system.get_balance("Bob")}")

    
    """
    Take-Home Challenge
        Advanced Escrow
        1. Integrate escrow into Phase 6 blockchain as OPEN_ESCROW and CLAIM_ESCROW transactions.
        2. Add partial claims (claim some, leave rest).
        3. BONUS: Create atomic swap between two escrows.
    """