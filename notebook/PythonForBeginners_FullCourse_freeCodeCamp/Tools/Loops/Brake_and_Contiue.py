# Loops - Brake and Continue

    # Continue stops the current loop and tells Python to execute the next one
    # Brake stops the loop altogether and goes on with the next instruction after the loop ends

items = [1, 2, 3, 4]

for item in items:
    if item == 2:
        continue
            # If the item is equal to 2, it skips that loop (doesn't print the item)            
    print(item)

for item in items:
    if item == 2:
        break
            # If the item is equal to 2, it breaks out of the loop and it isn't going to run another loop
    print(item)