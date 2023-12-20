class Computer:
    hdd = 1000
    ram = 16
    model = "HP 4215"
    power = 100
    is_turn_on = False

    def turn_on(self):
        self.is_turn_on = True
        self.power -= 1

comp = Computer()
print(comp.is_turn_on)
print(comp.power)

comp.turn_on()
print(comp.power)
print(comp.is_turn_on)