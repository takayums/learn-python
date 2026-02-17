# String

# print string
print("hello world")

# Assign String to a Variable
name = "M. Asraf T"
print(name)

# Multiline String
multiline = """
    Hello Everyone 
    Today I want to show you
    About my project
"""
print(multiline)

# String in Array
words = "Hello Baby!"
print(words[0])

# Looping String
for i in "Asraf":
    print(i)

# String Length
print(len(name))

# Checking String
print("Asraf" in name)  # Case Sansitive

# Cehc is Not Present String
print("asraf" not in name)


# Python Slicing
# Slicing String
text = "Hello Everyone"
print(text[3:5])

# Slicing From Start
print(text[:6])

# Slicing to End
print(text[5:])

# Slicing with Negative Value
print(text[-5:-2])


# Python Modify
# Upper Case
print(text.upper())

# Lower Case
print(text.lower())

# Removw Space on Start and On End
text2 = " Hahah Hahah "
print(text2.strip())

# Replace Character
print(text.replace("H", "W"))

# Split String to Array
print(text.split())

# Concate String
print('"' + text + text2 + '"')

# Formating String
age = 20
text3 = f"my age is {age} years old"
print(text3)

# Escape Character
statement = 'We are so called "Vikings" from north'
print(statement)
