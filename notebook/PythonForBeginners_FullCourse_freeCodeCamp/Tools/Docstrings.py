# Docstrings

# They're comments or descriptions of what is the concept or what am I looking at

"""Dog module

This module does ... bla bla bla and provides the following classes:

- Dog
...
"""
    # Description of what the file is all about

def increment(n):
    """Increment a number"""
        # Description of what the function is
    return n + 1

class Dog:
    """A class representing a dog"""
        # Description of what the class is
    def __init__(self, name, age):
        """Initialize a new dog"""
            # Description of what the method does
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("WOOF!")



# Python will process the docstrings
    # I can use the "help" global function to get the documentation for a class, method, function or module 
print(help(Dog))
