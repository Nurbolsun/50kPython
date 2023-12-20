def unpack(lst):
    for e in lst:
        if type(e) is list:
            unpack(e)
        else:
            print(e)

a = [4, 2, 4, [5, 7, 9], 25, [42, 15, [15, 25]]]

unpack(a)