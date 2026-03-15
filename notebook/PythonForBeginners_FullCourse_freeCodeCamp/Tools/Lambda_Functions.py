# Lambda Functions
    # Functions that have no name
    # They have only one expression as their body
    # They're defined using the "lambda" keyword



lambda num : num * 2
    # "argument" : "expression"
        # It must be a single expression
        # Just an expression, not a statement
            # An expression *returns* a value, a statement doesn't

# "lambda" functions can accept more arguments
lambda a, b : a * b

# "lambda" cant be called directly, but I can assign them to variables
multiply = lambda a, b : a * b
    # "lambda" function is assigned to the "multiply" variable

print(multiply(2, 4)) # 8
