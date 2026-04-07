import os

def generate_key(length):
    return os.urandom(length)

def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("The key must be the same length as the plaintext.")

    ciphertext = bytes([p ^ k for p, k in zip(plaintext.encode('utf-8'), key)])
    return ciphertext

def vernam_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("The key must be the same length as the ciphertext.")

    plaintext = ''.join([chr(c ^ k) for c, k in zip(ciphertext, key)])
    return plaintext

def main():
    plaintext = "This is another example of the Vernam cipher!"

    key = generate_key(len(plaintext))

    print("Generated Key (hex):", key.hex())

    ciphertext = vernam_encrypt(plaintext, key)
    print("Encrypted Ciphertext (hex):", ciphertext.hex())

    decrypted_text = vernam_decrypt(ciphertext, key)
    print("Decrypted Plaintext:", decrypted_text)

if __name__ == "__main__":
    main()