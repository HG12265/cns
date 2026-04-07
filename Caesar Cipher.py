text = input("Enter text: ")
s = 5
cipher = ""
for ch in text:
    if ch.isalpha():
        cipher += chr((ord(ch) - 97 + s) % 26 + 97)
    else:
        cipher += ch
print("Encrypted:", cipher)
plain = ""
for ch in cipher:
    if ch.isalpha():
        plain += chr((ord(ch) - 97 - s) % 26 + 97)
    else:
        plain += ch
print("Decrypted:", plain)
