import hashlib

def fingerprint(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


print(fingerprint("crypt"))
print(fingerprint("crypto"))
print(fingerprint("crypt"))
# same input delivers same output, slightly different input produces completely different output. 