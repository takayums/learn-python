# Createing Variable
print("")
print(10 * "=", "Createing Variable", 10 * "=")

x = 4
y = 5

print("Result 4 + 5 =", x + y)

# Casting Type Data
# Untuk memastikan tipe data sesuai kebutuhkan
print("")
print(10 * "=", "Casting Data Type", 10 * "=")

name = str(25)
grade = int("25")

print("This is string data type", name)
print("Result grade + x + y = ", grade + x + y)

# Aturan membuat variable
# 1. Diawali dengan _ atau huruf, bukan angka
# 2. Bisa berisi karakter tertentu
# 3. Case Sensitive, age dengan Age itu berbeda
# 4. Tidak berkaitan dengan keyward python

print("")
print(10 * "=", "Ruels Create Variable", 10 * "=")

_name = "Asraf"
fname = "muhammad"
Fname = "Muhammad"

print("Different result", _name, fname, Fname)

# Beberapa Cara agar Variable dapat mudah dibaca
# 1. Camel Case myName
# 2. Pascal Case MyName
# 3. Snake Case my_name

# Menugaskan Sekaligus Beberapa Variable
print("")
print(10 * "=", "Assign Multiple Vaues", 10 * "=")

gradeA, gradeB, gradeC = 90, 80, 75
print("Grade A", gradeA)
print("Grade B", gradeB)
print("Grade C", gradeC)

# Satu Nilai untuk Beberapa Variable
print("")
print(10 * "=", "Ruels Create Variable", 10 * "=")

valueA = valueB = valueC = "Value"
print(valueA)
print(valueB)
print(valueC)

# Unpack or Extrax Array / Tuppele
print("")
print(10 * "=", "Extrac Array / Tupple", 10 * "=")

result = ["Asraf", "Muhammad", "Takayums"]
resultA, resultB, resultC = result
print(resultA)
print(resultB)
print(resultC)


# Global Variable & Local
# Menggunakan Key Word "global"
print("")
print(10 * "=", "Global Variable", 10 * "=")


def sayHello():
    global names
    names = "Julia"


sayHello()
print("Name From Say Hello Function", names)
