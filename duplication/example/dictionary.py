# 辞書
dictionary = {
    "name": "John",
    "age": 20,
    "city": "New York"
}

print(dictionary)

name = dictionary["name"]

print(name)

dictionary["name"] = "Doe"

print(dictionary)

print(dictionary.get("name"))

print(dictionary.keys())

print(dictionary.values())

print(dictionary.items())

dictionary["new"] = "new"

print(dictionary)
