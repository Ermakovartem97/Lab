def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.

    """
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext = ciphertext + chr(ord(plaintext[i]) + 3)
    return ciphertext
def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    """
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext = plaintext + chr(ord(ciphertext[i]) - 3)
    return plaintext


a = encrypt_caesar("PYTHON")
print(a)
b = decrypt_caesar(a)
print(b)