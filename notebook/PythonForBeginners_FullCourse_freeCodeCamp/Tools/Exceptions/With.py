# Exceptions - With

# Helpful to simplify working with exception handling
    # Eg: when working with files, each time I open a file, I must remember to close it
        # "with" makes the process more transparent



# Long way:
filename = "/Users/falvio/test.txt"

try:
    file = open(filename, "r")
        # Opens the file
    content = file.read
        # Reads the file
    print(content)
        # Prints the file's content
finally:
    file.close()
        # Closes the file

# Short way:
filename = "/Users/falvio/test.txt"

with open(filename, "r") as file:
    content = file.read()
    print(content)