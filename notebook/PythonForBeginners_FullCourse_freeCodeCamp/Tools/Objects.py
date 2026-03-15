# Objects
    # Everything is an object, even values of basic prim of types like:
        #  integers, strings, floats, lists, tuples, dictionaries, etc.

# Objects have attributes and methods that can be accessed using the "dot" syntax



# Attributes for integers
age = 8

print(age.real)
print(age.imag)
print(age.bit_length())



# Attributes for lists
items = [1, 2]

items.append(3)
    # Adds the item to the end of the list
items.pop()
    # Deletes the (default) last item from the list and returns it

print(id(items))
    # Location in memory