# Polymorphism

# Generalizes a functionality so it can work on different types



# I define the same method (eat) on different classes
class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

# I create 2 objects
animal1 = Dog()
animal2 = Cat()

    # I can create an object and call the eat method regardless of the class the object belongs to
animal1.eat()
animal2.eat()

# I built a generalized interface and now I don't need to know that an animal is a cat or a dog,
    # I just need to know that I can call eat on it