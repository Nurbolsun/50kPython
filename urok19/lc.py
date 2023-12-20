a = [5, 3, 6, 4, 2]

# b = [] # [5, 6, 4]

# for e in a:
#     if e > 3:
#         b.append(e)
# print(b)

b = [e for e in a] # all add b
b = [e for e in a if e > 3] # [e for e in a if e > 3]
b = [e % 2 == 0 for e in a] # делятся ли на 2
print(b) 


c = 5
d = 15 if c > 3 else 25
print(d)



