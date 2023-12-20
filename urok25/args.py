def mysum(r, *args):
    for num in args:
        r += num
    return r

print(mysum(5, 2, 1))