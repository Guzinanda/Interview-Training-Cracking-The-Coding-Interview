"""
@   Is Unique | 1.1

@   Problem
    Implement and algorithm to determine is a strigs has all unique characters.
    What if you cannot use additional data structures?

@   Example
    Input:      str = Hi
    Output:     True

    Input:      str = Hello
    Output:     False

@   Template:
    01. Create a dictionary.
    02. I will iterate the string for each letter.
    03. I will save the letter in the dictionary if I dont previously have it
        if I already have that letter I will return False.

"""

def isUnique(string):

    letters = {}

    for letter in string:
        if letter in letters:
            return False
        
        letters[letter] = True
    return True


# TEST __________________________________________________________________________

str01 = "Hi"
print(isUnique(str01))

str02 = "Hello"
print(isUnique(str02))
