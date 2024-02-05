plain_txt = "APPLE".upper()
key = "LEM".upper()

padd_key = key
if len(plain_txt) == len(key):
    padd_key = key
else:
    for i in range(len(plain_txt)-len(key)):
        padd_key += key[i%len(key)]

print(padd_key)
print(plain_txt)
encrpyted = ""
for i in range(len(plain_txt)):
    encrpyted += chr(((ord(plain_txt[i]) + ord(padd_key[i])) % 26)+65)
print(f"after encrption : {encrpyted}")

print('decyprtion : ')
decrpyted = ""
for i in range(len(plain_txt)):
    decrpyted += chr(((ord(encrpyted[i]) - ord(padd_key[i])) % 26)+65)
print(f"after encrption : {decrpyted}")
