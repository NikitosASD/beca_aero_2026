# Modules

    # Every Python file is a module
    # I can import a module from other files (base of any program of moderate complexity)
    # Promotes a sensible organization and code reuse
    # It's basically how I can create a software that has multiple Python programs in the same piece of software
    
    # In the typical Python program, one file acts as the entry point,
        # and the other files are modules and exposed functions that I can call from other files



# Common libraries (modules):
#   - math for math utilities
#   - re for regular expressions
#   - json to work with JSON
#   - datetime to work with dates
#   - sqlite3 to use SQLite
#   - os for Operating System utilities
#   - random for random number generation
#   - statistics for statistics utilities
#   - requests to perform HTTP network requests
#   - http to create HTTP servers
#   - urllib to manage URLs



import dog
    # imports the "dog.py" file
dog.bark()
    # calls the "bark" function from the "dog.py" file

from dog import bark
    # imports *only* the "bark" function from the "dog.py" file
bark()
    # calls the imported "bark" function



from lib import dog2
    # imports the "dog2.py" file from the "lib" folder (the folder has to have a "__init__.py" file)
dog2.bark()
    # calls the "bark" function from the "dog2.py" file

from lib.dog2 import bark
    # imports *only* the "bark" function from the "dog2.py" file of the "lib" folder
bark()
    # calls the imported "bark" function



import math

print(math.sqrt(4)) # 2.0

from math import sqrt

print(sqrt(4)) # 2.0