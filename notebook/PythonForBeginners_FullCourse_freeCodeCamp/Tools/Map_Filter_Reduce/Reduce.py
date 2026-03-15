# Reduce()

# Reduce is used to calculate out of a sequence like a list

# Without reduce (long way):
expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]
    # List of "expenses" stored as tuples
    # I want to calculate the sum of the property (cost of the expense) in each tuple

sum = 0
for expense in expenses:
    sum += expense[1]

print(sum) # 200



# With reduce:
from functools import reduce

expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]
    # List of "expenses" stored as tuples
    # I want to calculate the sum of the property (cost of the expense) in each tuple

sum = reduce(lambda a, b : a[1] + b[1], expenses)
    # sum = reduce("reduction" function, iterable)
        # The function has to take two arguments:
            # First argument "a" is the accumulated value
            # Second argument "b" is the update value from the iterable

print(sum) # 200