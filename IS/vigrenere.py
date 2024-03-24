plain_txt = input("Enter plaintext : ").upper()
key = input("Enter Key : ").upper()
padd_key = key
if len(plain_txt) == len(key):
    padd_key = key
else:
    for i in range(len(plain_txt)-len(key)):
        padd_key += key[i%len(key)]

print(f"\nPlain Text : {plain_txt}\nKey : {key}\nPadded Key : {padd_key}\n")
print('encrption : ')
encrpyted = ""
for i in range(len(plain_txt)):
    encrpyted += chr(((ord(plain_txt[i]) + ord(padd_key[i])) % 26)+65)
print(f"after encrption, cipher text : {encrpyted}")
print('decyprtion : ')
decrpyted = ""
for i in range(len(plain_txt)):
    decrpyted += chr(((ord(encrpyted[i]) - ord(padd_key[i])) % 26)+65)
print(f"after decyprtion, decrypted text : {decrpyted}")
