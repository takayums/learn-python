# Json Python
import json

# json type
x = '{"name": "asraf", "age": 25}'

# convert json to object
y = json.loads(x)
print(y)

# convert to json
z = json.dumps(y)
print(z)
print(type(z))
