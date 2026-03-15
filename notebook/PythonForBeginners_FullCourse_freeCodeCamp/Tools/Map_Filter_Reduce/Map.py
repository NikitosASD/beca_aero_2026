# Map()

# Map is used to run a function upon each item in an iterable (loop) item like a list,
    # and create a new list with the same number of items but the values of eac item can be changed

numbers = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, numbers)

print(list(result)) # [2, 4, 6]


# Using "lambda" function
numbers = [1, 2, 3]

double2 = lambda a : a * 2

result = map(double2, numbers)

print(list(result)) # [2, 4, 6]


# More simplified
numbers = [1, 2, 3]

result = map(lambda a : a * 2, numbers)

print(list(result)) # [2, 4, 6]

# The original list is left untouched, and a new list with the updated values is returned by "map"