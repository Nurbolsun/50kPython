a = [2, 6, 4, 4]
my_sum = sum(a)
q = len(a)
print(my_sum/q)

def avg(lst):
    s = sum(lst)
    q = len(lst)
    sa = s / q
    return sa

print(avg(a))