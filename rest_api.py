from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import hashlib, time, uvicorn

class Block: 
    def __init__(self, index, transaction, previous_hash): 
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.hash = hashlib.sha256(f"{self.index}{self.transaction}{self.previous_hash}{self.timestamp}".encode()).hexdigest()
        
    def to_dict(self):
        return {"index": self.index, "transaction": self.transaction, "previous_hash": self.previous_hash, "hash": self.hash}
    

class Blockchain: 
    pass

class TxRequest(BaseModel): 
    pass

class FaucetRequest(BaseModel):
    pass

@app.get("/chain")
def get_chain():
    pass

@app.get("/balance/{address}")
def get_balance(address: str): 
    pass

@app.get("/transaction")
def add_tx(tx: TxRequest):
    pass

@app.get("/mine")
def mine(miner: str = Query(...)):
    pass

@app.post("/faucet")
def faucet(req: FaucetRequest):
    pass

if __name__ == "__main__":
    pass