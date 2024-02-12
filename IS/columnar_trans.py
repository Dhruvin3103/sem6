import math

pt = "ATTACKTHETARGETONNINE"
key = "APPLE"


def find_rank(key):
    rank = 0
    for i in sorted(key):
        key = key.replace(i, str(rank), 1)
        rank += 1
    key = [int(i) for i in key]
    return key


def encrypt(pt, key):
    cols = len(key)
    rows = math.ceil(len(pt) / cols)
    key_rank = find_rank(key)
    print(key_rank)
    pt += "".join(["X"] * (rows * cols - len(pt)))
    matrix = [list(pt[i : i + cols]) for i in range(0, len(pt), cols)]
    for i in range(rows):
        print(matrix[i])
    ciphertext = ["*" for i in range(cols)]
    j = 0
    for i in key_rank:
        ciphertext[i] = [row[j] for row in matrix]
        j += 1
    res = []
    for i in ciphertext:
        res.extend(i)
    return "".join(res)

def decrypt(cip, key):
    cols = len(key)
    rows = math.ceil(len(cip) / cols)
    key_rank = find_rank(key)
    print(key_rank)
    cip += "".join(["X"] * (rows * cols - len(cip)))
    matrix = ["*" for i in  range(rows)]
    for i in key_rank:
        matrix[i] = [list(cip[i : i + cols]) for i in range(0, len(cip), cols)]
    for i in range(rows):
        print(matrix[i])
    cip = ["*" for i in range(cols)]



ciphertext = encrypt(pt, key)
print(ciphertext)
decrypt(ciphertext, key)
