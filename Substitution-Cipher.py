import string

letters = string.ascii_letters
key = 4

# Encryption
plain = input("Enter text: ")
cipher = ""

for ch in plain:
    if ch in letters:
        index = letters.index(ch)
        cipher += letters[(index + key) % len(letters)]
    else:
        cipher += ch

print("Encrypted:", cipher)

# Decryption
decrypted = ""

for ch in cipher:
    if ch in letters:
        index = letters.index(ch)
        decrypted += letters[(index - key) % len(letters)]
    else:
        decrypted += ch

print("Decrypted:", decrypted)