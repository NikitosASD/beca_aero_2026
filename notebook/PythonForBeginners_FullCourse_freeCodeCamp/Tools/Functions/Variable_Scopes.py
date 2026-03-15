# Functions - Variable Scopes

age1 = 8
    # Es una variable global porque puedo usarla en cualquier código luego de la declaración
    # Puedo usarla en una función

def test():
    print(age1)

print(age1) # 8
test() # 8



def test2():
    age2 = 8
        # age sólo es visible dentro de la función
    print(age2)

print(age2)
    # Crea un error porque age2 no está definido (fuera de la función)
test2()