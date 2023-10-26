def fibonacci(n):
    print()
    fib = [0,1]

    while len(fib) < 10:
        nextNUmber = fib[-1]+fib[-2]
        fib.append(nextNUmber)
    else:
        return fib
n = 10
res = fibonacci(n)
print(res)