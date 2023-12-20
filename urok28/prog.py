
try:
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError:
    print("Операция не удалось")
    print("Делить на ноль нельзя")
except ValueError:
    print("Возможно ввод не верны")