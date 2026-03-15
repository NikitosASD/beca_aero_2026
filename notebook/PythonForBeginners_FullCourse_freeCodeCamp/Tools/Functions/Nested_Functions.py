# Functions - Nested Functions

    # A function defined inside a function is only visible inside that function
    # Useful to create utilities that are useful to a function but not useful outside of it

def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(" ")
    for word in words:
        say(word)

talk("I am going to buy the milk")
    # The frase is "I am going to buy the milk"
    
    # phrase.split(" ") creates a list of each the phrase separated by space (each word individually)
    # Then, for every word in the words list, it's going to say the word



def count():
    count = 0

    def increment():
        nonlocal count
            # "nonlocal" gives access to the *variable* "count" that is inside another *function*
            # If it isn't used, the *function* "increment" can't read the *variable* "count"
        count = count + 1
        print(count)
    
    increment()

count()