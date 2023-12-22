"""
Instructions: 
List: Rotate (⚡Interview Question)
You are given a list of n integers and a non-negative integer k.

Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.

The function should modify the input list in-place, and you should not return anything.

Constraints:

Each element of the input list is an integer.

The integer k is non-negative.



Function signature: def rotate(nums, k):

Example:

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Function call: rotate(nums, k)
Output: nums = [5, 6, 7, 1, 2, 3, 4]


Explanation: The list has been rotated to the right by 3 steps:



[7, 1, 2, 3, 4, 5, 6]

[6, 7, 1, 2, 3, 4, 5]

[5, 6, 7, 1, 2, 3, 4]
"""


def rotate(nums: list[int], k: int) -> None:
    # Calculate the effective number of steps to rotate
    k = k % len(nums)
    # Rearrange the elements in the rotated order
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""
