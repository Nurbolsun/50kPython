def mydivision(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivisionError("На ноль делить НЕЛЬЗЯ!")
    return num_1 / num_2

a = int(input())
b = int(input())

print(mydivision(a,b)) #ZeroDivisionError: division by zero