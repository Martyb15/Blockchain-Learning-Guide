from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import hashlib, time, uvicorn

class Block: 
    pass

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