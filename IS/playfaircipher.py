# key = input("Enter key : ").upper()
key = "DEMON"


import string

def make_matrix(key):
    letters = list(string.ascii_uppercase)
    for letter in key:
        if letter == 'I' or letter == 'J':
            letters.remove('I')
            letters.remove('J')
        else:
            letters.remove(letter)
        
    matrix = list(key)
    matrix.extend(letters)
    matrix = [matrix[i:i+5] for i in range(0,25,5)]
    return matrix

# word = input("Enter plaintext : ").upper()
word = "instruments".upper()
print(f"key: {key}\nplain text: {word}\n")

print(f"matrix : ")
cipher_matrix = make_matrix(key)
for row in cipher_matrix:
    print(row)

def create_pairs(word):
    pairs = []
    if len(word) % 2 != 0:
        word += word[-1]
    for i in range(0, len(word), 2):
        pair = word[i:i+2]
        pairs.append(pair)
    return pairs


def add_extra_character(word):
    result = ""
    # extra_char = find_missing_letters(word)
    for i in range(len(word) - 1):
        result += word[i]
        if word[i] == word[i + 1]:
            result += "X"
    result += word[-1]
    
    if len(result)%2!=0:
        result += "X"
    return result
    
result_word = add_extra_character(word)
result = create_pairs(result_word)

print(f"2pair of text : {result}")

mod_text = result

def search(matrix,elmt):
    # print(matrix,elmt)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # print(i,j)
            if matrix[i][j] == elmt:
                return i,j
    return 0,0
            

def playfair_encrypt(mat,txt):
    cipher = []
    for i in txt:
        a,b = search(mat,i[0])
        c,d = search(mat,i[1])
        print(a,b,c,d)
    
        if b == d:
            print('bd')
            word = ""
            if a+1>4:
                word += mat[0][b]
            else:
                word += mat[a+1][b]
            if c+1>4:
                word += mat[0][d]
            else:
                word += mat[c+1][d]
            cipher.append(word)
        
        elif a == c:
            print('ac')
            word = ""
            if b+1>4:
                word += mat[a][0]
            else:
                word += mat[a][b+1]
            if d+1>4:
                word += mat[c][0]
            else:
                word += mat[c][d+1]
            cipher.append(word)
        
        else:
            word = mat[a][d] + mat[c][b]
            cipher.append(word)
    return cipher

def playfair_decrypt(mat, txt):
    plaintext = []
    for i in txt:
        a, b = search(mat, i[0])
        c, d = search(mat, i[1])
        if b == d:  
            word = ""
            if a - 1 < 0:
                word += mat[4][b]
            else:
                word += mat[a - 1][b]
            if c - 1 < 0:
                word += mat[4][d]
            else:
                word += mat[c - 1][d]
            plaintext.append(word)

        elif a == c:  
            word = ""
            if b - 1 < 0:
                word += mat[a][4]
            else:
                word += mat[a][b - 1]
            if d - 1 < 0:
                word += mat[c][4]
            else:
                word += mat[c][d - 1]
            plaintext.append(word)

        else:
            word = mat[a][d] + mat[c][b]
            plaintext.append(word)

    return plaintext

cipher_txt = "".join(playfair_encrypt(cipher_matrix,mod_text))
print(f"Cipher Text is : {cipher_txt}")
decrypt_txt = "".join(playfair_decrypt(cipher_matrix, create_pairs(cipher_txt)))
print(f"Decrypted Text : {decrypt_txt}")
            
            
     
