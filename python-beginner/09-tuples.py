# Tuples Python
# Berurutan dan Tidak bisa dirubah
# Boleh memiliki nilai sama / duplikat
# Index dimulai dari 0
# Bisa berisi tipe data apa saja

myTuples: tuple[str, ...] = ("apple", "banana", "orange")

# panjang tuples
print(len(myTuples))

# type typles
print(type(myTuples))

# notTuples = ("apple")
# print(type(notTuples))

yesTuples = ("apple",)
print(type(yesTuples))

# akses item tupels
print(myTuples[1])

# akses item tupels dengan index nilai negativ
print(myTuples[-1])

# operasi range items sama seperti di list

# update tuples
# bisa di rubah dengan cara conver ke list dan nanti di convert lagi di tupl
listNew: list[str] = list(myTuples)
print(listNew)
print(type(listNew))

listNew[1] = "manggo"
myTuplesNew = tuple(listNew)

print(myTuplesNew)

# menambhkan items di tupples
myTuplesNew += yesTuples
print(myTuplesNew)

# menghapus item di tuple
# cara sama dengan mengupdate tuple, harus conver ke list dan kembali convert ke tuples

# unpacking tuple
fruit1, fruit2, fruit3 = myTuples
print(fruit1)
print(fruit2)
print(fruit3)

# unpacking tapi variable tidak bisa menampung semua isi dari tupe
fruitA, *fruitB = myTuplesNew
print(fruitA)
print(fruitB)  # menjadi list

# loop tuples
for i in range(len(myTuplesNew)):
    print(myTuplesNew[i])

# menggabungkan dua tuples
tuple1 = (1, 2, 3)
tuple2 = ("Asraf", "Adit", "Ardi")
tuple3 = tuple1 + tuple2
print(tuple3)

# metode pada tupple
# count -> menghitung nilai tersebut seberapa banyak
# index -> akses nilai berdasarkan index di tuples
