def generateKey(plainText, key):
    key = list(key)
    if len(plainText) == len(key):
        return "".join(key)
    else:
        for i in range(len(plainText) - len(key)):
            key.append(key[i % len(plainText)]) 
        return "".join(key)

def encrypt(plainText, key):
    cipherText = []
    for i in range(len(plainText)):
        x = (ord(plainText[i]) - 65) ^ (ord(key[i]) - 65)
        x += ord("A")
        cipherText.append(chr(x))
    return "".join(cipherText)

def decrypt(cipher, key):
    normal = []
    for i in range(len(cipher)):
        x = (ord(cipher[i]) - 65) ^ (ord(key[i]) - 65)
        x += ord("A")
        normal.append(chr(x))
    return "".join(normal)

    
plaintext=input("Enter the plaintext : ").upper()
key=input("Enter the key : ").upper()
print(f"Plain Text : {plaintext}\nKey:{key}\n")
key=generateKey(plaintext,key)
print("encrypted cipher text is : ",encrypt(plaintext,key))        
cipheredText=encrypt(plaintext,key)
print("decrypted text is : ",decrypt(cipheredText,key))  
