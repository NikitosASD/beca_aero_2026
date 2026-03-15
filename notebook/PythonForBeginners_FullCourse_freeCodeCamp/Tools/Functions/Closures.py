# Function - Closures

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
            # The function "increment" returns "count" from the nested function
    
    return increment
        # The function "counter" returns the function "increment()" (nested funcion) from the outer function

increment = counter()
    # Instead of calling the outter function directly, it assigns the function "counter()" to the variable

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3
    # I just call the variable which is the returned inner function (nested function) "increment()"
    # Because I call the inner function, it isn't going to reset the count to 0 and it can keep track of that value
        # I return the inner function "increment", and it still has access to the state of the "count" variable,
        # eventhough the function "counter" has ended