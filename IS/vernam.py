plain_txt = "OAK".upper()
key = "SON".upper()

padd_key = key
if len(plain_txt) == len(key):
    padd_key = key
else:
    for i in range(len(plain_txt) - len(key)):
        padd_key += key[i % len(key)]

print(padd_key)
print(plain_txt)
encrpyted = ""
for i in range(len(plain_txt)):
    if (ord(plain_txt[i])-65 ^ord(padd_key[i])-65)>26: 
        encrpyted += str((ord(plain_txt[i])-65 ^ord(padd_key[i])-65)-26) + " "
    else:
        encrpyted += str((ord(plain_txt[i])-65 ^ord(padd_key[i])-65)) + " "
print(f"after encrption : {encrpyted}")

print("decyprtion : ")
decrpyted = ""
for i in range(len(plain_txt)):
    if (ord(plain_txt[i])-65 ^ord(padd_key[i])-65)>26: 
        decrpyted += str((ord(encrpyted[i])-65 ^ord(padd_key[i])-65)-26) + " "
    else:
        encrpyted += str((ord(encrpyted[i])-65 ^ord(padd_key[i])-65)) + " "
print(f"after encrption : {encrpyted}")
