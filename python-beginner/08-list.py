# Python List
# Berisi tipe data apa saja
# Dapat dirubah
# Indexing
# Boleh memiliki nilai sama / duplikat
# Bisa memiliki satu type data yang sama

mix_data = ["banana", True, 1, "banana", "apple", "manggo", "orange"]

list1 = [True, False, True]

print(type(list1))

print(len(mix_data))


# Acces Items
print(mix_data[0])  # item pertama list

# Acces Items The Last
print(mix_data[-1])

# Range of Indexes / Slicing
# dimulai dari index 2 (inxluded) dan diakhiri sampai index 5 (not included)
print(mix_data[2:5])

# akses dari awal sampai index 4 (not included)
print(mix_data[:4])

# akses dari index tertentu sampai akhir
print(mix_data[2:])

# akses dengan index negative
print(mix_data[-4:-1])

# cek jika ada item dalam list
if "banana" in mix_data:
    print("Yes, I do find it")


# mengganti item
mix_data[1] = "Asraf"
print(mix_data)

# mengganti berdasarkan range
mix_data[2:4] = ["Aku", "Kamu"]
print(mix_data)

# jika data diganti lebih dari rang maka akan diletakkan setelahnya
mix_data[4:5] = ["We", "Oo"]
print(mix_data)

# jika data yang diganti kurang dari range maka data setelah yang diganti akan hilang
mix_data[5:7] = ["Ada"]
print(mix_data)

# menambbahkan bedasrakan index ke berapa
mix_data.insert(3, "Adit")
print(mix_data)


# menambahkan data
# tambahkan data diakhir list
mix_data.append("terakhir")

# menggabungkan dua list
mix_data.extend(list1)
print(mix_data)

# extend juga bisa digunakan menambahakn data seperti tupple, set, dan dictionary
mix_data.extend(("hore", "hai"))
print(mix_data)


# menghapus data di list
mix_data.remove("hai")
print(mix_data)

# menghapus data bedasarkan index berapa
mix_data.pop(1)
print(mix_data)

# hapus semua list
del mix_data
# print(mix_data) # tidak bisa diakses lagi karena sudah dihapus variabelnya

# menghapus semua isi list, tapi variable masih ada dan berisi list kosong
empty = ["Loha"]
empty.clear()
print(empty)


# loop di list
fruits = ["banana", "strowbarry", "manggo", "orang"]
for i in fruits:
    print(i)

for i in range(len(fruits)):
    print(fruits[i])

# list comperhansion
newlist = [x for x in fruits if "o" in x]
print(newlist)

# sort list
fruits.sort()  # asc
print(fruits)

fruits.sort(reverse=True)  # desc
print(fruits)

# copy list
newlist = fruits.copy()
print(newlist)
