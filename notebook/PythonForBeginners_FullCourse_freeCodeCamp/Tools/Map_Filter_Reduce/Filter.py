# Filter()

# Filter takes an iterable (loob) and returns a filter object,
    # which is another iterable (loop) but without some of the original items

# I can do so by returning true or false from the filtering function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(n):
    # Filtering function
    return n % 2 == 0
        # *If* the number is divisible by two, it is even, and it *returns* "true"
        # *If* the number is odd, it *returns* "false"


result = filter(isEven, numbers)

print(list(result)) # [2, 4, 6, 8, 10]

# Using simplified "lambda" function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result)) # [2, 4, 6, 8, 10]