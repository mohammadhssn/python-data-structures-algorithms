"""
Instructions: 
HT: First Non-Repeating Character (⚡Interview Question)
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""


def first_non_repeating_char(string):
    # create an empty hash table to count the frequency of each character
    char_counts = {}
    # count the frequency of each character in the string
    for char in string:
        # this increments the count by 1 in the dictionary
        char_counts[char] = char_counts.get(char, 0) + 1
    # find the first non-repeating character in the string
    for char in string:
        if char_counts[char] == 1:
            return char
    # return None if no non-repeating character is found
    return None
