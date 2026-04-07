def encrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha(): 
            base = 65 if ch.isupper() else 97
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch  

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  
text = input("Enter the plain text: ")
shift = 5

encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)