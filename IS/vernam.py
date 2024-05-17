def encDec(word,key):
    result=[]
    for i in range(len(word)):
        res=(ord(word[i])-97)^(ord(key[i])-97)
        result.append(chr((res)+97))
    return ''.join(result)
pt = "lifeisnoteasy"
key = "youneverknow"
pad_key = key
if len(pt) != len(key):
    for i in range(len(pt) - len(key)):
        pad_key += key[i % len(key)]
print(f"Key used is : {pad_key}")
result=encDec(word=pt,key=pad_key)
print(f'Encrypted:{result}\nDecrypted:{encDec(result,key=pad_key)}')
