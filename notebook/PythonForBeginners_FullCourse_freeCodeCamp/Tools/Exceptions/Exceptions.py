# Exceptions

# It's important to have a way to handle errors, and Python gives me "Exception" handling to do so



# I wrap lines of code in a "try" block and if an error occurs,
    # Python will alert me and I can decide which kind of error occured using an except block
        # I have to use an exact type of error
"""try: """
    # some lines of code
"""except <ERROR1>:"""
    # handler <ERROR1>
        # If <ERROR1> happens, I would handle that error
"""except <ERROR2>:"""
    # handler <ERROR2>
        # If <ERROR2> (a different error) happens, I would handle that different error
"""except:"""
    # Handles the rest of exceptions
"""else:"""
    # No exceptions were raised, the code ran succesfully
        # I can put else and then run a specific code at the bottom if there's no errors in the code
"""finally:"""
    # Do something in any
        # It's going to always run at the end whether or not there are exceptions or not
            # The code in the final block is always going to run



"""result = 2 / 0"""
    # It resulted in error, so it isn't going to run the following line of code (print)
"""print(result)"""



try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1

print(result) # 1



# I can also raise exceptions in my own code too
"""raise Exception("An error!")"""
    # Gives the hole exception message

# I can also intercept it and just show the "error" message
try:
    raise Exception("An error!")
except Exception as error:
    print(error)



class DogNotFoundException(Exception):
    pass
        # The "pass" is used when I define a class without methods or a function without code

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")