# Functions
#           - Decomposes a program into manageable parts
#           - Promotes readability and code reuse
#           - Name of function is very important
#           - It should be descriptive so anyone calling it can imagine what it does
#           - Can accept one or more parameters ()

def hello(): 
    print("Hello!")
        # Function *named* hello, with a *body* that prints "Hello!"

hello()
hello()
hello()
    # Call the function (Run the function so it does what its *body* says)



def hello(name):
    print("Hello " + name)
        # The function has the parameter "name"

hello("Beau")
hello("Quincy")
    # Call the function with parameter "name" replaced by new *argument* "Beau" and "Quincy"
#       - *Parameters are the values accepted by the function, inside the function definition*
#       - *Arguments are the values we pass to the function when we call it*



# hello()
    # Gives an error because there is no *argument* that replaces the parameter *name*
#       - *Arguments can have a default value that's applied if the argument is not specified*

def hello(name = "my friend"):
    print("Hello " + name)
        # If i don't put an argument, it's going to default to "my friend"

hello("Beau")
hello("Quincy")
hello()



def hello(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old!")
        # Two parameters

hello("Nico", 20)
        # Two arguments



    # If an object is *immutable*:
        # What I change *in* the function doesn't affect what is *outside* the function

def change(value):
    value = 2
        # Function with parameter "value" = 2

val = 1
change(val)
    # Call change with a new parameter "val" = 1 ("value" is still equal to 2)

print(val)
    # Prints 1


    # If an object is *mutable*:
        # What I change *in* the function does affect what is *outside* the function

def change(value):
    value["name"] = "Syd"
        # Function with parameter "value" that changes value of the key "name" to "Syd"

val = {"name": "beau"}
    # val is a new parameter that is a dictionary with key "name" and value "beau"

change(val)
    # Call *change* for dictionary "val" and it changes the value of the key "name" 

print(val)
    # Prints dictionary with {"name": "Syd"}

def hello(name):
    print("Hello " + name + "!")
    return name
        # Returns the "name" and the I can continue to use in the program
        #   - Returns anything that happens inside the function
        #   - When the function meets the return, it ends
hello("Nico")

def hello(name):
    if not name:
        return
#   - I can put a return in an "if" and put code in the "else" so it continues on the condition
#   - The return can be alone with nothing else and just end the function

    print("Hello " + name + "!")
        # No hace falta el "else"
hello(False)
    # No hay "name", no devuelve nada
hello("Beau")
    # Hay "name", devuelve el print



def hello(name):
    print("Hello " + name + "!")
    return name, "Beau", 8

print(hello("Syd"))
        # El parametro name se cambia por el argumento "Syd"
        # La función realiza Hello Syd! y devuelve "Syd", "Beau", 8
        # Luego imprimo el valor que me devuelve la función hello ("Syd", "Beau", 8)



