# Oprator Python

# Operator Aritmatika
x = 10
y = 35

print(x + y)
print(x - y)
print(x * y)
print(x**y)
print(x % y)
print(x / y)
print(x // y)

# Operator Assigment
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
print(x := 3)
x &= 3
print(x)

# Oprator Komparasi
m = 5
n = 4

print(m == n)
print(m != n)
print(m > n)
print(m < n)
print(m <= n)
print(m >= n)

# Operator Logical
print(m > n and m < n)
print(m < n or m > n)
print(not (m > n and m < n))

# Operator Identify
# is or is not
dicA = ["apple", "banana"]
dicB = ["apple", "banana"]
dicC = dicA

print(dicA is dicB)
print(dicA is dicC)  # Object yang Sama
# is tidak sama dengan ==
# is mengecek bedasarkan kesamaan memory, nilai variabel yang disimpan pada memory yang sama

# Membership Operator
# in or not in
fruits = ["apple", "banana", "manggo"]
print("banana" in fruits)
print("orange" not in fruits)

# Operator Bitwise
print(3 & 4)

# Operator Presedence
print(8 * 9 - 10 / 30)
