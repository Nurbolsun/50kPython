from myfunction import mysum
#from myclass import A # import from myclasses.py
from myclasses.first_class import A
from myclasses.second import B


print(mysum(1, 2, 5))

my_object = A()
my_object_b = B()

print(my_object.a, my_object_b.b)