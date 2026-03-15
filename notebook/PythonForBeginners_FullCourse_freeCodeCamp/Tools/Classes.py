# Classes
    # I can declare my own classes and, from the classes, I can instantiate object
        # An object is an instance of a class
        # A class is the type of an object



class Dog:
    # class "name of class" (Dog)
    def bark(self):
            # "self" is an argument of the method, and will point to the current object instance
            # It must be specified when defining a method
        print("woof!")

roger = Dog()

print(type(roger))
    # "roger" is a "Dog" class (roger is a dog)



# Constructor to initialize one more properties when I create a new object from that class
class Dog:
    def __init__(self, name, age):
            # "name" and "age" are 2 variables i can pass in when I create a dog,
                # and it will be associated with that object
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)
    # When I create this dog, it's going to assign the "name" to "self.name" and the "age" to "self.age"

print(roger.name) # Roger
    # "self" is "roger" and I do "self.name"

print(roger.age) # 8

roger.bark() # woof!



# Important feature of Class: "Inheritance"

class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    # "Dog" class is going to "inherit" from "Animal" class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)


print(roger.name)
print(roger.age)

roger.bark()
roger.walk()

# "Dog" class doesn't have a walk method, but it's getting it from the "Animal" class
    # It's "inheriting" this method
    # I can create a "Cat" class, "Duck" class and they can inherit the walk method