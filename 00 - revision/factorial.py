# def factorial(n):
#     print(n)
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=5
# result=factorial(n)
# print(result)

def factorial(n):
    p = 1
    for i in range(1,n+1):
        p = p *i
    return p
n=5
result=factorial(n)
print(result)