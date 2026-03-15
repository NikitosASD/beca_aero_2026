# Loops

condition = True
while condition == True:
    print("The first condition is True")
    condition = False

    # While the condition is true, keep running the code inside the loop



count = 0
while count < 10:
    print("The condition is True")
    count += 1

print("After the loop")



items = [1, 2, 3, 4]
for item in items:
    print(item)



for item in range(15):
    print(item)



items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)
    # Prints the index (vector) and its item



items = ["beau", "syd", "quincy"]
for index, item in enumerate(items):
    print(index, item)
