def multipler(n):
    return lambda k: k*n

doubler = multipler(2)
tripler = multipler(3)

print(doubler(6))
print(tripler(6))