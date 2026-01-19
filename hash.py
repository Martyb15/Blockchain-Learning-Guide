import hashlib

def fingerprint(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


print(fingerprint("crypt"))
print(fingerprint("crypto"))
print(fingerprint("crypt"))
# same input delivers same output, slightly different input produces completely different output. 

"""
Take-Home Challenge

The Avalanche Effect Explorer
1. Write a program that takes a string and shows how many characters change in the hash when you
modify just ONE character in the input.
2. Compare SHA-256 with MD5 (hashlib.md5). Which produces longer hashes? Research: why is MD5
considered insecure today?
3. BONUS: How many hashes can your computer calculate per second? Write a benchmark.
"""