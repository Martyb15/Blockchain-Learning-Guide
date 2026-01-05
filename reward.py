# Why would anyone spend electricity mining? Because they get paid! Each block includes a special
# "coinbase" transaction that creates new coins and gives them to the miner.

BLOCK_REWARD = 50

class Blockchain:
    def mine_block(self, miner_address: str):
        # create reward transactions (money from nowhere)
        reward = Transaction(
            sender = "SYSTEM",
            recipient = miner_address,
            amount = BLOCK_REWARD, 
            signature = "GENESIS"      #Special Case
        )

        # Add reward to the block
        transactions = self.pending_transactions + [reward]

        # Mine it
        block = Block(transactions, self.chain[-1].hash)
        block.mine()

        # Add to chain and credit miner
        self.chain.append(block)
        self.balances[miner_address] = \
            self.balances.get(miner_address, 0) + BLOCK_REWARD
        
        print(f"Miner earned {BLOCK_REWARD} coins!")



"""
Take-Home Challenge


Bitcoin Economics
1. Implement 'halving': every 10 blocks, cut the reward in half (50 → 25 → 12.5...).
2. Add transaction fees to the miner's reward (sum of all fees in the block).
3. Calculate: if reward halves every 10 blocks, what's the maximum total supply?
4. BONUS: Create a get_total_supply() method that counts all coins ever created.




What you learn:
• New coins are created as mining rewards
• This is how Bitcoin/Ethereum create new currency
• Miners compete because they want the reward
"""
