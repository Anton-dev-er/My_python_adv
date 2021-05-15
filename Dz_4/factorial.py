def generator(n):
    f = 1
    i = 1
    while n > 0:
        f = f * i
        yield f
        n -= 1
        i += 1


gen = generator(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
