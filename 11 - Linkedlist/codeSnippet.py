def funv(a, b):

    a = a+4
    b  = b.append(5)
    return(a,b)

a = 11
b = [4]
(funv(a,b))
print(a)
print(b)

# 1, [5]

# mutable = list, dict,set -->value can change 
# immutabele = tuple, string, int, boolean, float --> literals --> you cant change