matrix = [
#j-> 0  1  2   #i
    [5, 2, 8], #0
    [4, 3, 0], #1
    [9, 4 ,6]  #2
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(i, j, matrix[i])