# Encapsulatioon Python

# Melindungi data propertis dan fungsi agar tidak dirubah dengan seenaknya
# Perubahan harus menggunakan metode tertentu, biasanya menggunakan getter dan setter


class Rekening:
    def __init__(self, name, saldo):
        self.name = name
        self.__saldo = saldo

    def __privet_method(self):
        print("method privet")

    def getter_saldo(self):
        print(self.__saldo)

    def setter_saldo(self, nominal):
        self.__saldo += nominal

    def akses_method_prive(self):
        self.__privet_method()


r1 = Rekening("Mandiri", 500000)
print(r1.name)
# print(r1.__saldo) # tidak bisa diakses untuk properties saldo
r1.getter_saldo()  # aksess dengan fungsi gatter
r1.setter_saldo(100000)  # rubah dengan fungsi setter
r1.getter_saldo()
r1.akses_method_prive()
