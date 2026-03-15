# Sets (Just one of each item) (If i put "Roger" twice, it only reads it once)

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2
    # Intersección (deben contener lo mismo)
print(intersect)



set1 = {"Roger", "Syd"}
set2 = {"Luna"}

mod = set1 | set2
    # Unión (combina todo su contenido)
print(mod)



set1 = {"Roger", "Syd"}
set2 = {"Roger"}

dif = set1 - set2
    # Diferencia (elimina el mismo contenido)
print(dif)



set1 = {"Roger", "Syd"}
set2 = {"Roger"}

mod = set1 > set2
    # Does "set1" have everything and more than "set2" ? (True)
print(mod)



print(list(set1))
    # Gives a list of the items in a set