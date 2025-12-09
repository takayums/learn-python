name = "Asraf"
age = 25

message = "Nama saya "+ name + ", umur " + str(age) # harus di konvert supaya bisa gabung
print(message)

# Len String
print("panjang string name", len(name))

# Acces Charackter based Index
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Slicing String
print(name[:2])
print(name[1:3])
print(name[1:4])

print(name[:])
print(name[1:])
print(name[:4])

# String Method
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
print(name.capitalize())
print(name.count("a"))
print(name.replace("A", "z"))
print(name.find("f"))


# Escape Characters
statement = "Baris pertama \n Baris baru"
print(statement)

statement2 = "Name:\tAsraf\nAge:\t25"
print(statement2)

statement3 = "root:\\takayumadev\\Dev"
print(statement3)

statement4 = "Dia berkata \"Hello Gaes\""
print(statement4)

statement5 = "I\'m new student"
print(statement5)

# String Interpolataion
data = f"Hello bro my name is {name}, and I\'m {age} years old."
print(data)

# String Interpolataion Expression
print(f"Hello world, I\'m {age*10} years old")
print(f"Uppercase Name {name.upper()}")
