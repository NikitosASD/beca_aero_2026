# Recursion

# Recursion is a function in Python that calls itself
    # It can be explained using the factorial calculation

def factorial(n):
    if n == 1: return 1
        # Always has the base case (if n == 1: return 1)
            # It's when I am going to leave the recursive function
    return n * factorial(n-1)
        # if n != 1 --> Recursive case (return n * factorial(n-1) )

print(factorial(3))
print(factorial(4))
print(factorial(5))
