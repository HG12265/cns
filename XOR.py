def encryptDecrypt(text):
    xorKey = 'H'
    result = ""

    for ch in text:
        result += chr(ord(ch) ^ ord(xorKey))

    return result

sampleString = input("Enter the plain Text: ")

encrypted = encryptDecrypt(sampleString)
print("Encrypted string:", encrypted)

decrypted = encryptDecrypt(encrypted)
print("Decrypted string:", decrypted)