def armstrong(a):
    b = str(a)
    s = 0
    for i in b:
        c = len(b)
        s  = s+int(i)**(c)
    return a == s

a = 1634
armstrong(a)
if armstrong(a):
    print("yes it is armstrong")
else:
    print("not an armstronkm fdkljb ndfknbo")
