"""
Instructions: 
HT: Two Sum (⚡Interview Question)
two_sum()

Problem: Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

Input:

A list of integers nums .

A target integer target.

Output:

A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].



Example:



Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add up to the target 9.
 
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: The numbers at indices 1 and 2 in the array add up to the target 6.
 
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add up to the target 6.
 
Input: nums = [1, 2, 3, 4, 5], target = 10
Output: []
Explanation: There are no two numbers in the array add up to the target 10.
 
Input: nums = [], target = 0
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].
"""

def two_sum(nums: list[int], target: int) -> list:
    # create an empty hash table
    num_map = {}
 
    # iterate through each number in the array
    for i, num in enumerate(nums):
        # calculate the complement of the current number
        complement = target - num
 
        # check if the complement is in the hash table
        if complement in num_map:
            # if it is, return the indices of the two numbers
            return [num_map[complement], i]
 
        # add the current number and its index to the hash table
        num_map[num] = i
 
    # if no two numbers add up to the target, return an empty list
    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))



"""
    EXPECTED OUTPUT:
    ----------------
    [0, 1]
    [1, 2]
    [0, 1]
    []
    [2, 3]
    [0, 1]
    []

"""
