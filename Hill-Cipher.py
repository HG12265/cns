def hillCipher(message, key):
    # convert key into 3x3 matrix
    keyMatrix = []
    k = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.append(ord(key[k]) - 65)
            k += 1
        keyMatrix.append(row)

    # convert message into vector
    messageVector = []
    for i in range(3):
        messageVector.append(ord(message[i]) - 65)

    # multiply matrix
    cipherVector = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            cipherVector[i] += keyMatrix[i][j] * messageVector[j]
        cipherVector[i] %= 26

    # convert to text
    cipherText = ""
    for i in range(3):
        cipherText += chr(cipherVector[i] + 65)

    print("Ciphertext:", cipherText)


# Main
message = input("Enter 3-letter message: ").upper()
key = input("Enter 9-letter key: ").upper()

hillCipher(message, key)