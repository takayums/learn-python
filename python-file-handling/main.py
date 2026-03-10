f = open("demofile.txt")
print(f.read())

print(type(f.read()))
f.close()
# rekomendasi mengguankan with

with open("demofile.txt") as f:
    print(f.read())

# w parameter menandakan untuk mengooverite isi file yang sudah ada dengan yang baru
# with open("demofile.txt", "w") as fw:
#     fw.write("Overite file old")
#

# a parameter digunakan untuk menulis tulisan baru di file yang sudah ada isinya
with open("demofile.txt", "a") as fa:
    fa.write("\n")
    fa.write("Add On New Line in File")

with open("demofile.txt") as f:
    print(f.read())

# delete file
import os

if os.path.exists("demofilee.txt"):
    os.remove("demofilee.txt")
else:
    print("File tidak ditemukan")
