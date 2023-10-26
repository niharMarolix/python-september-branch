# a = (1,2,3)
# print(type(a))

a = ()
# print(type(a))

b = list(a)
b.append(1)

a = tuple(b)
print(a)
print(type(a))