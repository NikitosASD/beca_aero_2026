# Dictionaries

dog = { "name": "Roger", "age": 8 }
    # Dictionary

dog["name"] = "Syd"
    # Changes "name" value to "Syd"

print(dog.get("name"))
    # Gives only the value of "name"



print(dog.get("color", "brown"))
    # Doesn't find "color" in dog, so it defaults to brown

dog = { "name": "Roger", "age": 8 , "color": "green"}
    # New dictionary with "color" key

print(dog.get("color", "brown"))
    # If it finds "color", it returns the dictionary value for "color" (green)



print(dog.pop("name"))
    # It substracts and prints only the value of "name"
print(dog)
    # It prints the rest of the dictionary



dog = { "name": "Roger", "age": 8 , "color": "green", "weight": "14kg"}
    # New dictionary with "weight" key

print(dog.popitem())
    # It substracts the last key and its value
print(dog)
    # It prints the rest of the dictionary



print("color" in dog)
    # Checks if the key "color" is in dog (True)



print(dog.keys())
    # Prints only the dict_keys

print(list(dog.keys()))
    # Prints only the keys (as a list)



print(dog.values())
    # Prints only the dict_values

print(list(dog.values()))
    # Prints only the values (as a list)



print(dog.items())
    # Prints only the dict_items (as the keys and its values)

print(list(dog.items()))
    # Prints only the keys and its values (as a list)



print(len(dog))
    # Prints the number of items in dog



dog["favourite food"] = "Meat"
    # Adds a new item with a key and its value ("Meat")
print(dog)

del dog["color"]
    # Deletes an item
print(dog)

dogCopy = dog.copy()