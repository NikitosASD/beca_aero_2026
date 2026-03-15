# Accepting Arguments



##########

import sys

print(sys.argv)

    # In powershel or cmd terminal write:
        # python (folders)\\filename.py item item item ...
    
    # Gives list of ["filename.py", "item", "item", "item"]



import sys

name = sys.argv[1]

print("Hello " + name)
    # Prints "Hello " and the "name" I put as an item

########## Delete for "argparse"



import argparse

parser = argparse.ArgumentParser(
    description="This program prints the name of my dogs"
        # Desription of the program
)

# Arguments I want to accept:
parser.add_argument("-c", "--color", metavar="color", required=True, help="the color to search for")
    # For this program, I accept the -c or --color and I call it "color" (metavar)

args = parser.parse_args()

print(args.color)
    # I can access arg.color to get the color that was passed in,
        # and then I can specify whether it's required and what help is going to go along that

    # In powershel or cmd terminal write:
        # python (folders)\\filename.py -c (or --color, and then the) color



import argparse

parser = argparse.ArgumentParser(
    description="This program prints the name of my dogs"
)

parser.add_argument("-c", "--color", metavar="color", required=True, choices={"red", "yellow"}, help="the color to search for")
    # I can set an option to have a specific set of values using "choices"

args = parser.parse_args()

print(args.color)

    # In powershel or cmd terminal write:
        # python (folders)\\filename.py -c (or --color, and then the) color (from the choices)