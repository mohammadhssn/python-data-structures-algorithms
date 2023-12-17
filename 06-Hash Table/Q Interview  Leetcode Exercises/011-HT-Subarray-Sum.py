"""
Instructions: 
HT: Subarray Sum (⚡Interview Question)
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:

nums: a list of integers representing the input array

target: an integer representing the target sum


Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.

For example:



nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))  # should print [1, 3]
"""

def subarray_sum(nums: list[int], target: int) -> list:
    # create an empty hash table and set the initial sum and index
    sum_index = {0: -1}
    current_sum = 0
 
    # loop through each number in the input array
    for i, num in enumerate(nums):
        # add the number to the current sum
        current_sum += num
 
        # check if the difference between the current sum and the target sum has been seen before
        if current_sum - target in sum_index:
            # return the indices of the subarray that adds up to the target sum
            return [sum_index[current_sum - target] + 1, i]
 
        # add the current sum and its index to the hash table
        sum_index[current_sum] = i
 
    # if no subarray is found, return an empty list
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
