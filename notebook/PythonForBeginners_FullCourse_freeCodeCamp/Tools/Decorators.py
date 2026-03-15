# Decorators

# They're a way to change, enhance or alter in any way how a function works
# Decorators are defined with the "@" symbol, followed by the decorator name just before the function definition
# A decorator is a function that takes another function as a parameter,
    # wraps the function in an inner function that performs the job it has to do,
        # and returns that inner function

def logtime(func):
    def wrapper():
        print("before")
            # do something before
        val = func()
        print("after")
            # do something after
        return val
    return wrapper


@logtime
def hello():
    print("Hello")
# When I call the function, the decorator is going to be called too

hello()

# I am going to often use "decorator" functions whe I want to change the behavior of a function,
    # without modifying the function itself

# Eg: When I want to add logging test performance, perform caching, verify permissions, etc.
# Eg: Whe I need to run the same code on multiple functions