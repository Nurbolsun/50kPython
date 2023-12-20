fib = [1, 1]
n = 35

for i in range(n):
    new = fib[i] + fib[i+1]
    fib.append(new)

print(fib)
