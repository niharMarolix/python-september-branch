a = (1,2,4,)
print(type(a))


print(a[0])
print(a[1:2])
print(len(a))

print(4 in a)

b = a + (6,7)

print(b)

for items in b:
    print(items)