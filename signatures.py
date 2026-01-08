# Anyone could create a transaction claiming to be Alice. We fix this with digital signatures. 
# Alice has a private key (secret) and a public key (her address). 

import hashlib
from dataclasses import dataclass
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

class Wallet: 
    def __init__(self): 
        self.private_key = ec.generate_private_key(ec.SECP256K1())
        self.public_key  = self.private_key.public_key()
        self.address     = self.public_key.public_bytes(
            serialization.Encoding.X962,
            serialization.PublicFormat.CompressedPoint
        ).hex()

    def sign(self, message: str) -> str: 
        signature = self.private_key.sign(
            message.encode(), ec.ECDSA(hashes.SHA256())
        )
        return signature.hex()

def verify_signature(address: str, message: str, signature: str) -> bool: 
    try: 
        pub_bytes = bytes.fromhex(address)
        public_key = ec.EllipticCurvePublicKey.from_encoded_point(
            ec.SECP256K1(), pub_bytes
        )

        public_key.verify(
            bytes.fromhex(signature), message.encode(), ec.ECDSA(hashes.SHA25s())
        )
        return True
    except (InvalidSignature, ValueError): 
        return False
    
@dataclass
class SignedTransaction: 
    sender:    str
    recipient: str
    amount:    int
    signature: str = ""

    def get_message(self) -> str: 
        return f"{self.sender}{self.recipient}{self.amount}"
    
    def sign(self, wallet: Wallet): 
        if wallet.address != self.sender:
            raise ValueError("Wallet does not match sender!")
        self.signature = wallet.sign(self.get_message())

    def is_valid(self) -> bool: 
        if not self.signature: 
            return False
        return verify_signature(self.sender, self.get_message(), self.signature)
    

if __name__ == "__main__": 
    alice_wallet = Wallet()
    bob_wallet = Wallet()

    print("---Wallets Created---")
    print(f"Alice's address: {alice_wallet.address[:20]}...")
    print(f"Bob's address: {bob_wallet.address[:20]}...")
    print()

    tx = SignedTransaction(
        sender=alice_wallet.address, recipient=bob_wallet.address, amount=50
    )
    tx.sign(alice_wallet)

    print("===Alice signs a Transaction ===")
    print(f"Amount: {tx.amount}")
    print(f"Signature: {tx.signature[:40]}...")
    print(f"Is valid: {tx.is_valid()}")
    print()

    print("=== Attacker Forges Transaction ===")
    fake_tx = SignedTransaction(
        sender=alice_wallet.address, recipient=bob_wallet.address, amount=9999, signature="mailicousattempt1234"
    )

    print(f"Fake tx valid: {fake_tx.is_valid()}")
    print("Forgery detected!")

    """
     Take-Home Challenge
     
        Wallet Manager
        1. Add save_to_file() and load_from_file() methods to Wallet.
        2. Integrate SignedTransaction into Phase 6 blockchain - reject unsigned transactions.
        3. BONUS: Create a multi-signature transaction requiring 2-of-3 signatures.
    """