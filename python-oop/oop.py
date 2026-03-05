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


class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)


c1 = Car("Ford")
c1.show()
