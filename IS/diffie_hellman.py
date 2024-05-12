def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primitive_check(g, p, list=[]):
    for i in range(1, p):
        list.append(pow(g, i) % p)
    for i in range(1, p):
        if list.count(i) > 1:
            return -1
        return 1   
while True:
    p=int(input("Enter values of p:"))
    g=int(input("Enter values of g:"))
    if (is_prime(p) and primitive_check(g,p)):
        a=int(input("Enter values of a:"))
        b=int(input("Enter values of b:"))
        if a >= p or b >= p:
            print(f"Private Key Of Both The Users Should Be Less Than {p}!")
        else:
            XA,XB=(g**a) % p  , (g**b) % p
            AK,BK = (XB**a) % p  , (XA**b) % p
            print(f"\nSecret Key For User 1 Is {AK}\nSecret Key For User 2 Is {BK}\n")
            print("Keys Have Been Exchanged Successfully") if AK == BK else print("Keys Have Not Been Exchanged Successfully")
            break    
    else:
        print("enter correct values")
