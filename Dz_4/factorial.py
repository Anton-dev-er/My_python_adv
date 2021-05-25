def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        yield f


f = factorial(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
