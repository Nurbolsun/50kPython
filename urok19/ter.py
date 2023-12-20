a = [4, 2, 5, 6]
b = [num   if num > 3 else 10   for num in a]  # a = [4, 10, 5, 6]
print(b)