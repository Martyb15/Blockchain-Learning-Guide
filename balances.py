# A blockchain is also a state machine. We need to track balances and reject transactions from people who do not have enough funds. 
from transactions import Transaction

class SimpleChain: 
    def __init__(self):
        self.chain = []
        self.balances = {}


    def set_balance(self, address: str, amount: int):
        self.balances [address] = amount

    def add_block(self, transactions: list[Transaction]):
        for tx in transactions:
            # check if sender has enought funds
            if self.balances.get(tx.sender, 0) < tx.amount:
                print(f"Rejected: {tx.sender} is broke!")
                continue

            #move money
            self.balances[tx.sender]    -= tx.amount
            self.balances[tx.recipient] = \
                self.balances.get(tx.recipient, 0) + tx.amount

if __name__ == '__main__':
            
    chain = SimpleChain()
    chain.set_balance("Alice", 100)
    chain.add_block([Transaction("Alice", "Bob", 50)])
    print(chain.balances)
    

""""
Take-Home Challenge

Build a Mini Bank
1. Add a get_balance(address) method that returns 0 for unknown addresses.
2. Implement fees: subtract (amount + fee) from sender, give fee to a 'MINER' address.
3. Add a transfer(sender, recipient, amount) method that creates and processes a transaction in one call.
4. BONUS: Prevent negative balances AND prevent overflow (numbers too large).
"""