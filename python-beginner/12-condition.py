# Condition in Python

# if, elif, and else
temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")

# shorthand condition
(
    print("A")
    if temperature > 30
    else (
        print("B")
        if temperature > 20
        else print("C") if temperature > 10 else print("D")
    )
)

# logical operator
score = 11
if score >= 0 and score <= 100:
    print("Valid Score")
else:
    print("Invalid Score")

# nested condition
x = 20

if x >= 10:
    if x > 20:
        print("Nilai Diatas 20")
    else:
        print("Nilai antara 10 - 20")

# pass
# menandakan tidak ada action, jika masuk pada condisi terpenuhi
if x > 5:
    pass
