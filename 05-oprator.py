# Operator
a = 5
b = 10

print("=== Operator ====")
print(f"Penjumlahan a + b = {a+b}")
print(f"Pengurangan a 0 b = {a-b}")
print(f"Pembagian a / b = {a/b}")
print(f"Perkalian a * b = {a*b}")

print("\n")
print("=== Operator Penugasan ====")
x = 10
print(f"nilai x = {x}")
x += 5
print(f"x setelah += 5 {x}")
x -= 5
print(f"x setelah -= 5 {x}")
x *= 5
print(f"x setelah *= 5 {x}")
x /= 5
print(f"x setelah /= 5 {x}")

print("\n")
print("=== Operator Perbandingan ====")
print(f"nilai a = {a} \nnilai b = {b}")
print(f"a > b = {a>b}")
print(f"a < b = {a<b}")
print(f"a >= b = {a>=b}")
print(f"a <= b = {a<=b}")
print(f"a == b = {a==b}")
print(f"a != b = {a!=b}")

print("\n")
print("=== Operator Logika ====")
print(f"nilai b > a and b < 15 => {b > a and b < 15}")
hari = "Sabtu"
print(f"'Sabtu' == hari or 'Minggu' == hari => {"Sabtu" == hari or "Minggu" == hari}")
aktif = True
print(f"not Aktif => {not aktif}")


print("\n")
print("=== Operator String ====")
fname = "Asraf"
lname = "Takayuma"
print(fname + " " + lname)
print(fname * 3)
kalimat = "Python adalah bahasa pemrograman untuk pemula"
print("Python" in kalimat)
