class Car: #class
    maker = ""
    model = ""
    weight = 2000

    def __init__(self, **kwargs): #method
        self.maker = kwargs["maker"]
        self.model = kwargs["model"]

    def add(self, kg):
        self.weight += kg

    def __str__(self):
        return self.maker
    
class MersedesBenz(Car): #extendet / наследование
    maker = "Mersedesaa"
    def __init__(self, **kwargs):
        model = kwargs["model"]
        super().__init__(model=model, maker = self.maker)

lada = Car(model = "Lada", maker = "Kalina")
print(lada.weight)
lada.add(30)
print(lada.weight)
print(lada)

mers = MersedesBenz(model="S600", maker = "MersedesBenz")
print(mers)
mers.add(170)
print(mers.weight)