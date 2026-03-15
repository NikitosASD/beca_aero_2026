# Operator Overloading

# Advanced technique I can use to make classes comparable and to  make them work wit Python operators



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        # "__gt__" is going to compare things as to figure out what is greater than 
        return True if self.age > other.age else False

# I can use operator overloading to add a custom way to compare these two objects based on the age property
roger = Dog("Roger", 8)
syd = Dog("Syd", 7)

print(roger > syd) # True



# I can create methods that go with different arithmetic operators:
#   - __add__() responds to the + operator
#   - __sub__() responds to the - operator
#   - __mul__() responds to the * operator
#   - __truediv__() responds to the / operator
#   - __floordiv__() responds to the // operator
#   - __mod__() responds to the % operator
#   - __pow__() responds to the ** operator
#   - __rshift__() responds to the >> operator
#   - __lshift__() responds to the << operator
#   - __and__() responds to the & operator
#   - __or__() responds to the | operator
#   - __xor__() responds to the ^ operator