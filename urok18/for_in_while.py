m = [5, 2, 5, 3, 7, 15, 3, 1]
k = []

while m:     #sort to k[]
    c = m[0]
    for e in m:
        if c < e:
            c = e
    k.append(c)
    m.remove(c)
print(k)        

# c = m[0]
# for num in m:
#     if num > c:
#         c = num
# print(c)

# max = max(m)
# print(max)

# min = min(m)
# print(min)