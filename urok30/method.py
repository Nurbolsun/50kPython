class Car:
    maker = ""

    def __init__(self, model, maker) :
        self.model = model
        self.maker = maker
    def __str__(self):
        return f"{self.maker} {self.model}"
    
p = Car("644", "Porche")
print(p)