"""
Instructions: 
List: Find Max Min (⚡Interview Question)
Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.

The function should have the following signature:

def find_max_min(myList):


Where myList is the list of integers to search for the maximum and minimum values.

The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.

For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value.

"""

def find_max_min(myList: list[int]) -> tuple[int, int]:
    # Initialize the maximum and minimum variables 
    # to the first element of the list
    maximum = minimum = myList[0]
    
    # Traverse the list and update the 
    # maximum and minimum variables
    for num in myList:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    
    # Return the maximum and minimum variables
    return maximum, minimum


print(find_max_min([5, 3, 8, 1, 6, 9]))


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""
