def inside():
    print("123")
    print(4566)

def outside(f):
    f()

outside(inside)