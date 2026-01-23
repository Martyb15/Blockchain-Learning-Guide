# phase_12
import hashlib
import time
from dataclasses import dataclass, field
from typing import List, Set

@dataclass 
class Block:
    index: int
    data:  str
    previous_hash: str
    timestamp: float = field(default_factory=time.time)
    hash: str = ""

    def __post_init__(self): 
        pass

    def compute_hash(self) -> str: 
        pass


class Node: 
    def __init__(self, name: str): 
        self.name = name
        self.chain: List[Block] = []
        self.peers: Set['Node'] = set()
        self.pending_message: List[dict] = []
        genesis = Block(0, "Genesis", "0", 0)
        self.chain.append(genesis)

    def connect(self, peer: 'Node'): 
        pass

    def broadcast(self, message: dict): 
        pass

    def receive(self, message: dict, sender: 'Node'): 
        pass

    def process_message(self): 
        pass

    def create_block(self, data: str) -> Block: 
        pass


class Network: 
    def __init__(self): 
        pass
    
    def add_node(self, name: str) -> Node:
        pass

    def tick(self): 
        pass



# === Run Demo ===
if __name__ == "__main__": 
    pass