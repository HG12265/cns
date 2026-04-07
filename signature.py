from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Message
msg = b"Hello"

# Sign the message
signature = private_key.sign(
    msg,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Verify the signature
try:
    public_key.verify(
        signature,
        msg,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Valid Signature")
except:
    print("Invalid Signature")