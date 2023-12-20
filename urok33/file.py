f = open('example.txt')

# print(f.readlines())
#for line in f:
#    print(line)

for i in range(len(f.readlines())):
    print(f.readline())