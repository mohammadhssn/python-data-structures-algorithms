"""

Constraints:



The input list is sorted in non-decreasing order.

The input list may contain duplicates.

The function should have a time complexity of O(n), where n is the length of the input list.

The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new lists.



Example:

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] Function call: new_length = remove_duplicates(nums) Output: new_length = 5 Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)

Explanation: The function modifies the original list nums in-place, moving unique elements to the beginning of the list, followed by duplicate elements. The new length returned by the function is 5, indicating that there are 5 unique elements in the list. The first 5 elements of the modified list nums are the unique elements [0, 1, 2, 3, 4].



This code:



nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


Should Output:



New length: 5
Unique values in list: [0, 1, 2, 3, 4]
"""


def remove_duplicates(nums: list[int]) -> list[int] | int:
    # Return 0 if input list is empty
    if not nums:
        return 0
 
    # Initialize write_pointer at index 1
    write_pointer = 1
 
    # Loop through list starting from index 1
    for read_pointer in range(1, len(nums)):
        # Check if current element is unique
        if nums[read_pointer] != nums[read_pointer - 1]:
            # Move unique element to write_pointer
            nums[write_pointer] = nums[read_pointer]
            # Increment write_pointer for next unique element
            write_pointer += 1
 
    # Return new length of list with unique elements
    return write_pointer
    

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""

