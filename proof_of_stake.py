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
        if self.balances.get(address, 0) < amount: 
            print(f"Failes: {address} has insufficient balance")
            return False
        self.balances[address] -= amount 
        if address in self.validators: 
            self.validators[address].stake += amount
        else: 
            self.validators[address] = Validator(address, amount)
        print(f"STAKED: {address} locked {amount} coins")
        return True

    def select_validator(self) -> str: 
        total_stake = sum(v.stake for v in self.validators.values())
        if total_stake == 0 :
            return None
        pick = random.uniform(0, total_stake)
        current = 0
        for address, validator in self.validators.items(): 
            current += validator.stake
            if current >= pick:
                return address
        return list(self.validators.keys())[-1]
    
    def create_block(self) -> str: 
        validator_addr = self.select_validator()
        if not validator_addr: 
            return None
        validator = self.validators[validator_addr]
        reward = int(validator.stake * STAKE_REWARE_PERCENT)
        self.balances[validator_addr] = self.balances.get(validator_addr, 0) + reward
        validator.blocks_created += 1
        print(f"BLOCK: {validator_addr} created block, earned {reward} coins")

    def slash(self, address: str, percent: int = 50): 
        if address not in self.validators: 
            return 
        validator = self.validators[address]
        penalty = validator.stake * percent // 100
        validator.stake -= penalty
        print(f"SLASHED: {address} lost {penalty} coins")

    
# Running Demo
if __name__ == "__main__":
    pos = ProofOfStake()
    pos.set_balance("Alice", 1000)
    pos.set_balance("Bob", 500)
    pos.set_balance("Carol", 200)

    print("=== Staking Phase ===")
    pos.stake("Alice", 500)
    pos.stake("Bob", 300)
    pos.stake("Carol", 100)

    print()
    print("=== Creating 10 Blocks ===")
    selections = {"Alice": 0, "Bob": 0, "Carol": 0}

    for _ in range(10): 
        winner = pos.create_block()
        selections[winner] += 1
    
    print()
    print("=== Selections Statistics ===")
    total_stake = 500 + 300 + 100
    for name, count in selections.items(): 
        stake = pos.validators[name].stake
        expected = stake / total_stake * 100
        print(f"{name}: {count}/10 blocks, stake share {expected:.0f}%")

    print("=== Slashing Demo ===")
    pos.slash("Carol", 50)

