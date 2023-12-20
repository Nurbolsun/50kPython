a = [6, 2, 52, 25]

for i in range(len(a)):
    print(a[i])

for n in a[0:2]: #from 1  to 2  [::2] через 2  []
    print(n)

for index, element in enumerate(a): # with index and elemt
    print(index, element)