# Anotations

# Python is dynamically typed,
    # So I don't have to specify the type of a variable or function parameter or function return value

# Annotations allow me to optionally specify that
    # If I want to show actually what type I'm expecting for different values



# I specify that this function receives an "int" and is also going to return an "int"
def increment(n: int) -> int:
    return n + 1

# Can also be done for variables, I specify that this variable is goint to be an "int"
count: int = 0