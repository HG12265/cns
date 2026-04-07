import hashlib

msg = input("Enter message: ")

# SHA-256
sha256 = hashlib.sha256(msg.encode()).hexdigest()
print("SHA-256:", sha256)

# SHA-1
sha1 = hashlib.sha1(msg.encode()).hexdigest()
print("SHA-1:", sha1)