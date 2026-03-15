# List Compressions

#    It's sometimes preferred over loops as it's more readable when the operation can be written on a single line



numbers = [1, 2, 3, 4, 5]

# Short way:
numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

# Long way:
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

# More complex (unnecessary)
numbers_power_2 = list(map(lambda n : n**2, numbers))