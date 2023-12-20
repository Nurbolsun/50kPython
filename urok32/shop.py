class Good:
    is_sold = False
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sell(self, money_object):
        self.is_sold = True
        money_object.money += self.price
        return money_object

class Computer(Good):
    hdd = 1000
    is_licence = True

    def __init__(self, price, model):
        name = f"Computer {model}"
        super().__init__(name=name, price=price)

class Laptop(Computer):
    def __init__(self, price, model):
        name = f"Laptop {model}"
        super(Computer, self).__init__(name=name, price=price)

class Printer(Good):
    def __init__(self):
        name = "Printer LaserJet"
        price = 15560
        super().__init__(name, price)


class Money:
    money = 0


p_1 = Printer()
p_2 = Printer()

c_1 = Computer(1000, "AMD 451212")
c_2 = Computer(price=1000, model="AMD 451212")
c_3 = Computer(1500, "XyperX 4570")

l_1 = Laptop(1200, "ACER Aspire")

m = Money()


print(m.money)
m = c_2.sell(m)
print(m.money)


m = p_1.sell(m)
print(m.money)