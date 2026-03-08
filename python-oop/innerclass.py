# Inner Class Python
class Mahasiswa:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop("Lenovo", 64)

    class Laptop:
        def __init__(self, merk, ram):
            self.merk = merk
            self.ram = ram

        def speck_info(self):
            print("=== SPEK LAPTOP ===")
            print("Merk:", self.merk)
            print("Ram:", self.ram)


m1 = Mahasiswa("Asraf")
print("Mahasiswa", m1.name)
m1.laptop.speck_info()
