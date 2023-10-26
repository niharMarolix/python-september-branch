a = "csddvcdvcvdsdc"
b = list(a)
l = len(b)
emLIst = []
for i in range(l-1,-1,-1):
    emLIst.append(b[i])
    print(emLIst)

# print(emLIst)

print("".join(emLIst))