class Computer:
    hdd = 1000
    ram = 16
    model = "HP 4215"
    power = 100
    is_turn_on = False

    def turn_on(self):
        self.is_turn_on = True
        self.power -= 1

hp_1 = Computer()
print(hp_1.ram)

hp_2 = Computer()
print(hp_2.model)