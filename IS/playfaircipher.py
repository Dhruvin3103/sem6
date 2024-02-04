key = 'CIPHER'

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

print(f"matrix : {make_matrix(key)}")
cipher_matrix = make_matrix(key)
word = 'crpytography'.upper()

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
    extra_char = find_missing_letters(word)
    for i in range(len(word) - 1):
        result += word[i]
        if word[i] == word[i + 1]:
            while extra_char in result or extra_char == word[i]:
                extra_char = chr(ord(extra_char) + 1)
            result += extra_char
    result += word[-1]
    
    if len(result)%2!=0:
        result += extra_char
    return result
    
def find_missing_letters(word):
    all_letters = set("abcdefghijklmnopqrstuvwxyz")
    word_letters = set(word.lower())
    missing_letters = all_letters - word_letters
    return sorted(list(missing_letters))[0]
result_word = add_extra_character(word)
result = create_pairs(result_word)

print(f"2pair of text : {result}")

mod_text = result

def search(matrix,elmt):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == elmt:
                return i,j
            

def playfair(mat,txt):
    cipher = []
    for i in txt:
        a,b = search(mat,i[0])
        c,d = search(mat,i[1])
        
        if b == d:
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
        
        elif b+1 == c or b == c+1:
            word += mat[a]
    return cipher

print(playfair(cipher_matrix,mod_text))
            
            
     

