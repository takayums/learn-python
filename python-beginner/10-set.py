# Set Python
# Tidak urut
# Tidak bisa duplikat / unik
# Dapat dirubah

mysets = {"asraf", "dika", "radit"}
print(
    mysets
)  # ketika di print urutan data tidak sama seperti data dimasukkan, alias acak

setsDuplikat = {
    "asraf",
    "rino",
    "dika",
    "asraf",
}  # nilai duplikat akan dihapus salah satu
print(setsDuplikat)

# Nilai True itu sama dengan 1 begitu juga dengan nilai False sama dengan 0

# check type data set
print(type(setsDuplikat))

# access items
for x in mysets:
    print(x)

# check existing data in set
print("asraf" in mysets)

print("asraf" not in mysets)

# add item in set
mysets.add("wokowi")
print(mysets)

# update item / combined between set
mysets.update(setsDuplikat)
print(mysets)

# remove item in set
# mysets.remove("adit")  # jika data yang akan dihapus tidak ada, akan mengembalikan error
print(mysets)

mysets.discard(
    "asraf"
)  # jika data yang akan dihapus tidak ada, tidak masalah alias tidak menimbulkan error
print(mysets)

# metod metod dalam set
# pop
mysets.pop()  # remove random data from set

# clear
mysets.clear()  # mengosongkan isi dari set
print(mysets)

# del
del mysets  # menghapus variabel dari set itu sendiri

# menggabungkan 2 set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

print(set1.union(set2))
# set3 = set1 | set2 # | sama dengan tanda union
# set1.union(set2, set3, set4) # bisa menerima multiple set

# jika tidak ingin merubah set awal maka gunakan set.update
set1.update({"h", "w", "k"})
print(set1)

# menggabungkan dengan mengambil nilai / item yang sama dari kedua set
set4 = {"apple", "manggo", "orang", "banana"}
set5 = {"carry", "apple", "banana"}
set6 = set4.intersection(set5)  # atau bisa mengguankan set4 & set5
print(set6)

# mengamblikan nilai yang tidak sama diantara kedua set
set7 = set4.difference(set5)
print(set7)
