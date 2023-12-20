a = [
    [4, 2, 3],
    [5, 8, 0]
]

b = [e   for e_l in a   for e in e_l if e > 3]
print(b)