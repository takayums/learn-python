# OOP Python
# Object Oriented Programming

# Keuntungan OOP
# 1. Memberikan struktur yang bersih pada program
# 2. Membuat kode jadi mudah, reusable, dan debug
# 3. DRY (Don't Repeat Your Code)

# OOP terdiri dari
# 1. Object
# 2. Class


# Membuat Class
class Person:
    name = "Noname"


# Membuat Object
asraf = Person()
print(asraf.name)


# Mendelete Object
# del asraf


# Init Methode
class Animal:
    # multiple parameter and default value
    def __init__(self, name, beranak, berbulu=True):
        self.name = name
        self.beranak = beranak
        self.berbulu = berbulu

    def intro(self):
        return f"Aku {self.name}"

    # jika memanggil atribut / properties dari class harus menggunakan self
    def description(self):
        print(
            f"Aku adalah {self.name} dan aku hewan {"beranak" if self.beranak == True else "bertelur"} dan aku hewan {"berbulu" if self.berbulu == True else "tidak berbeulu"}"
        )

    # Memanggil methode dengan self
    def greet(self):
        greeting = self.intro()
        print("Haii!!", greeting)


h1 = Animal("Gajah", True, False)
h1.greet()
h1.description()

h2 = Animal("Ayam", False)
h2.greet()
h2.description()


# Class Properties and Object Properties
class Car:
    car_type = ""  # class properties

    def __init__(self, brand):
        # object properties
        self.brand = brand

    def show(self):
        print(self.brand)


c1 = Car("Ford")
c1.color = "Blue"
c1.show()
print(c1.color)
Car.car_type = "Toyota"
print(Car.car_type)


class Person:
    def __init__(self, name):
        self.name = name

    # str -> when print Object
    def __str__(self):
        return f"Name properties is {self.name} "

    # class method
    def greet(self):
        print("Hello, my name is", self.name)

    # method with parameter
    def check_health(self, is_sick):
        # modified properties
        self.name = "People"
        print(f"{self.name} is {"Sick" if is_sick == True else "Good"}")


p1 = Person("Daniel")
p1.greet()
p1.check_health(False)
print(p1)
