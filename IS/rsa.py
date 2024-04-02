def rsa(p,q,e,msg):
    # p = 7
    # q = 11
    # p,q = int(input("Enter p : ")), int(input("Enter q : "))
    n = p * q
    # e = int(input(f"Enter e relatively prime to {(p-1)*(q-1)}: "))
    phi = (p - 1) * (q - 1)
    d = 1
    while True:
        if (d * e) % phi == 1:
            break
        d += 1
    # msg = int(input("Enter the length of message : "))
    print(f"p : {p}, q : {q}, message bits : {msg}, e:{e}")
    print(f"Public key : {(e,n)}\nPrivate Key : {(d,n)}\n")
    print("Message data = ", msg)
    c = (msg**e) % n
    print("Encrypted data = ", c)
    m = (c**d) % n
    print("Original Message Sent = ", m)
    