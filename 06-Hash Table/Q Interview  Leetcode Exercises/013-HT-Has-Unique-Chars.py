"""
Instructions: 
Set: Has Unique Chars (⚡Interview Question)
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
"""

def has_unique_chars(string: str) -> bool:
    # Create an empty set to store characters
    char_set = set()
    # Loop through each character in the string
    for char in string:
        # Check if the character is already in the set
        if char in char_set:
            # If it is, return False (the string has duplicate characters)
            return False
        # If the character is not in the set, add it to the set
        char_set.add(char)
    # If we get to the end of the string without finding duplicates, return True
    return True


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False
"""
