def encrypt(text,s):
    result = ""
    for char in text:
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char)-base + s)%26+base) if (char.isupper()) else chr((ord(char)-base + s)%26+base)
    return result
def decrypt(text,s):
    result = ""
    for char in text:
        base = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - base - s) % 26 + base)
    return result
text = "ATTACKAToNCEY"
s = 4
cipherText=encrypt(text,s)
print (f"Text:{text}\nShift:{s}\nCipher:{cipherText}\nDecrypted:{decrypt(cipherText,s)}")
