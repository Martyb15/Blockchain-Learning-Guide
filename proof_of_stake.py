import random
from dataclasses import dataclass
from typing import Dict

STAKE_REWARE_PERCENT = 0.02

@dataclass
class Validator:
    address:        str
    stake:          int
    blocks_created: int = 0

class ProofOfStake:
    def __init__(self): 
        self.validators: Dict[str, Validator] = {}
        self.balances:   Dict[str, int] = {}

    def set_balance(self, address: str, amount: int): 
        self.balances[address] = amount

    def stake(self, address: str, amount: int) -> bool: 
        pass

