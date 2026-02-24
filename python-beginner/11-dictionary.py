# Dictionary Python
# Terdidi dari key dan value
# Teerurut dan tidak bisa duplikat
# Dapat dirubah, tambah, remove, dan update data

dict1 = {"fname": "Asraf", "lname": "Takayuma"}
print(dict1)

# length
print(len(dict1))

# type
print(type(dict1))

# acces items
print(dict1["lname"])

# get keys dict
print(dict1.keys())

# get value dict
print(dict1.values())

# get items
print(dict1.items())

# ceck key in dict
if "fname" in dict1:
    print("Ada")

# update dict
dict1["fname"] = "Muhammad"
print(dict1)

# update II
dict1.update({"mname": "Asraf"})
print(dict1)

# add items
dict1["fullname"] = "Muhammad Asraf Takayuma"
print(dict1)

# remove item dict
dict1.pop("fname")
print(dict1)

dict1.clear()
print(dict1)

del dict1
# print(dict1) # error, dict sudah dihapus dari memeroy

# loop dict
dict2 = {"first_name": "Adit", "last_name": "Ferry", "full_name": "Adit Ferry"}
print(dict2)

for i in dict2:
    print(i)

# copy dict
# dictcopy = dict2  => ini tidak bisa, karena dictcopy hanya mereference ke dict2
dictcopy = dict2.copy()
print(dictcopy)

# nested dict
myFamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

print(myFamily)
print(myFamily["child1"]["name"])
