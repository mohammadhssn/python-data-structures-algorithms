"""
Instructions: 
HT: Find Duplicates (⚡Interview Question)
find_duplicates()


Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


Input:

A list of integers nums.


Output:

A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].



Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in the input array.
"""

def find_duplicates(nums: list) -> list:
    # create an empty hash table
    num_counts = {}
 
    # iterate through each number in the array
    for num in nums:
        # add the number to the hash table or increment its count if it's already in the hash table
        num_counts[num] = num_counts.get(num, 0) + 1
 
    # create a list of the numbers that appear more than once in the input array
    duplicates = [num for num, count in num_counts.items() if count > 1]
 
    # return the list of duplicates
    return duplicates


print( find_duplicates([1, 2, 3, 4, 5]))
print( find_duplicates([1, 1, 2, 2, 3]))
print( find_duplicates([1, 1, 1, 1, 1]))
print( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print( find_duplicates([]))



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
