# parent class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


# child class
class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(
            self, fname, lname
        )  # cara lama untuk menurunkan properties di child class
        # super().__init__(fname, lname) -> penulisan terbaru tanpa menuliskan nama parent
        self.year = year

    def welcome(self):
        print(f"Selamat data {self.fname} {self.lname} to the class of {self.year}")


s1 = Student("asraf", "takayuma", 2019)
print(s1.fname)
print(s1.year)
s1.welcome()
