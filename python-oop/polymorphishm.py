class Vehical:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Move!")


class Car(Vehical):
    pass


class Boat(Vehical):
    def move(self):
        print("Sail!")


class Plane(Vehical):
    def move(self):
        print("Fly!")


c1 = Car("Ford", "Mustang")
b1 = Boat("Ibiza", "Touring 20")
p1 = Plane("Boeing", "747")

for x in (c1, p1, b1):
    print(x.model)
    print(x.brand)
    x.move()
