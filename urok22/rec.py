def my_print(n):
    if n > 5:
        print(n, " >> 5")
    else:
        print(n, " < 5")
    if n > 0:
        my_print(n-1)

my_print(10)