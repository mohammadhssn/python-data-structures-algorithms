"""
Instructions:
Stack: Reverse String (⚡Interview Question)
The reverse_string function takes a single parameter string, which is the string you want to reverse.

Return a new string with the letters in reverse order.

This will use the Stack class we created in the last three coding exercises: 30, 31, 32
"""


from typing import Any


class Stack:
    def __init__(self) -> None:
        self.stack_list = []

    def print_stack(self) -> None:
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self) -> bool:
        return len(self.stack_list) == 0

    def peek(self) -> None | Any:
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self) -> int:
        return len(self.stack_list)

    def push(self, value) -> None:
        self.stack_list.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            return None
        return self.stack_list.pop()
    

def reverse_string(string: str) -> str:
    stack = Stack()
    reversed_string = ""

    for char in string:
        stack.push(char)
        
    while not stack.is_empty():
        reversed_string += stack.pop()
        
    return reversed_string
    

my_string = 'hello'

print(reverse_string(my_string))


"""
    EXPECTED OUTPUT:
    ----------------
    olleh
"""
