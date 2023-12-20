def test(**kwargs):
    print(kwargs)
    print(**kwargs)

test()

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(4,5,6,7, k=15, t="Hello")