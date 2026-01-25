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
        self.hash = self.compute_hash()

    def compute_hash(self) -> str: 
        content = f"{self.index}{self.data}{self.previous_hash}{self.timestamp}"
        return hashlib.sha256(content.encode()).hexdigest()

class Node: 
    def __init__(self, name: str): 
        self.name = name
        self.chain: List[Block] = []
        self.peers: Set['Node'] = set()
        self.pending_message: List[dict] = []
        genesis = Block(0, "Genesis", "0", 0)
        self.chain.append(genesis)

    def connect(self, peer: 'Node'): 
        self.peers.add(peer)
        peer.peers.add(self)
        print(f"{self.name} <-> {peer.name} connected") 

    def broadcast(self, message: dict): 
        for peer in self.peers:
            peer.receive(message, self)

    def receive(self, message: dict, sender: 'Node'): 
        self.pending_messages.append({"msg": message, "from": sender.name})

    def process_message(self): 
        for item in self.pending_messages:
            msg = item["msg"]
            if msg["type"] == "new_block":
                b = msg["block"]
                new_block = Block(b["index"], b["data"], b["previous_hash"], b["timestamp"])
                if new_block.index == len(self.chain):
                    if new_block.previous_hash == self.chain[-1].hash:
                        self.chain.append(new_block)
                        print(f" {self.name}: Accepted block {new_block.index}")
        self.pending_messages.clear()

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