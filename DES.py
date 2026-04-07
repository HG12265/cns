from Crypto.Cipher import DES

# Padding function (adds spaces)
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

# Encryption
def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    return cipher.encrypt(padded_text)

# Decryption
def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted.rstrip(b' ')   # remove padding


# Main
key = b'secretke'   # must be 8 bytes
plaintext = b"This is a secret message"

ciphertext = encrypt(key, plaintext)
decrypted_text = decrypt(key, ciphertext)

print("PlainText:", plaintext)
print("CipherText:", ciphertext)
print("Decrypted Text:", decrypted_text)