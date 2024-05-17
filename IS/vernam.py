def encDec(word,key):
    result=[]
    for i in range(len(word)):
        res=(ord(word[i])-97)^(ord(key[i])-97)
        result.append(chr((res)+97))
    return ''.join(result)
result=encDec(word='lifeisnoteasy',key='youneverknoww')
print(f'Encrypted:{result}\nDecrypted:{encDec(result,key="youneverknoww")}')
