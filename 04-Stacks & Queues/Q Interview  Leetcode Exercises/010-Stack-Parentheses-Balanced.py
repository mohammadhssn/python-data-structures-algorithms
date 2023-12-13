"""
Instructions:
Stack: Parentheses Balanced (⚡Interview Question)
Check to see if a string of parentheses is balanced or not.

By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

Function name:
is_balanced_parentheses

Remember: this is not a method within the Stack class, this is a separate function.
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
    
    def is_balanced_parentheses(self, parentheses: str) -> bool:
        for p in parentheses:
            if p == "(":
                self.push(p)
            elif p == ")":
                if self.is_empty() or self.pop() != "(":
                    return False
        return self.is_empty()
    

balanced_parentheses = '((()))'
unbalanced_parentheses = '((())))'

my_stack = Stack()
print(my_stack.is_balanced_parentheses(balanced_parentheses))
print(my_stack.is_balanced_parentheses(unbalanced_parentheses))


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""
