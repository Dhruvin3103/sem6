import random
def isprime(n):
    if n <=1: return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True 
    
def gcd(a,b):
    while b!=0:
        a, b = b, a %b 
    return a
    
def generate_pr_no():
    while True:
        a = random.randint(100,1000)
        if isprime(a):
            return a
            
def generate_keys():
    p = generate_pr_no()
    q = generate_pr_no()
    n = p*q
    phi = (p-1)*(q-1)
    print(f"p:{p}, q:{q}, n:{n}, phi:{phi}")
    e = random.randint(1,phi)
    while gcd(e,phi) !=1:
            e = random.randint(1,phi)
    d = pow(e, -1, phi)
    return (e,n),(d,n)
    

public_key, private_key = generate_keys()
pt = 17
ct = (pt ** public_key[0]) % public_key[1]
print(f"ct : {ct}")
dt = (ct ** private_key[0]) % private_key[1]
print(f"dt : {dt}")
        
