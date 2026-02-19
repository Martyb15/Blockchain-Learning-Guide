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
    def __init__(self): 
        self.chain = [Block(0, [], "0")]
        self.pending = []
        self.balances = {}
    
    def add_transaction(self, sender, recipient, amount): 
        if sender != "SYSTEM" and self.balances.get(sender, 0) < amount:
            return False
        self.pending.append({"sender": sender, "recipient": recipient, "amount": amount})
        return True

    def mine(self, miner): 
        reward = {"sender": "SYSTEM", "recipient": miner, "amount": 50}
        txs = self.pending + [reward]
        block = Block(len(self.chain), txs, self.chain[-1].hash)
        for tx in txs: 
            if tx["sender"] != "SYSTEM": 
                self.balances[tx["sender"]] -= tx["amount"]
            self.balances[tx["recipient"]] = self.balances.get(tx["recipient"], 0) + tx["amount"]
            self.chain.append(block)
        self.pending = []
        return block
    
app = FastAPI(title="Mini Blockchain API")
blockchain = Blockchain()

class TxRequest(BaseModel): 
    sender: str
    recipient: str
    amount: int

class FaucetRequest(BaseModel):
    address: str
    amount: int = 100

@app.get("/chain")
def get_chain():
    return [b.to_dict() for b in blockchain.chain]

@app.get("/balance/{address}")
def get_balance(address: str): 
    return {"address": address, "balance": blockchain.balances.get(address, 0)}

@app.get("/transaction")
def add_tx(tx: TxRequest):
    if not blockchain.add_transaction(tx.sender, tx.recipient, tx.amount): 
        raise HTTPException(400, "Insufficient Funds")
    return {"status": "pending"}

@app.get("/mine")
def mine(miner: str = Query(...)):
    if not blockchain.pending: 
        raise HTTPException(400, "No Transactions")
    return {"block": blockchain.mine(miner).to_dict()}

@app.post("/faucet")
def faucet(req: FaucetRequest):
    blockchain.balances[req.address] = blockchain.balances.get(req.address, 0) + req.amount
    return {"address": req.address, "balance": blockchain.balances[req.address]}

if __name__ == "__main__":
    print("Visit http://localhost:5000/docs")
    uvicorn.run(app, host="0.0.0.0", port=5000)


"""
Take-Home Challenge
Build a Block Explorer
1. Add GET /address/{addr}/history for all transactions for an address.
2. Add GET /pending to show unconfirmed transactions.
3. Create a simple HTML page that displays the chain.
4. BONUS: Add websocket support for real-time updates.
"""