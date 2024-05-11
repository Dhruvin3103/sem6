def encDec(word,key):
    result=[]
    for i in range(len(word)):
        res=(ord(word[i])-65)^(ord(key[i])-65)
        if res>25:
            res%=26
        result.append(chr((res)+65))
    return ''.join(result)
result=encDec(word='RAMSWARUPK',key='RANCHOBABA')
print(f'Encrypted:{result}\nDecrypted:{encDec(result,key='RANCHOBABA')}')
