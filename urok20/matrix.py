a = [
    [5, 2, 4, 6, 2],
    [5, 2, 4, 6, 2],
    [5, 2, 4, 6, 2],
    [5, 2, 4, 6, 2]
]
b = []
for element_list in a:
    b.append([])
    for num in element_list:
        c = num * 10
        b[-1].append(c)

print(b)