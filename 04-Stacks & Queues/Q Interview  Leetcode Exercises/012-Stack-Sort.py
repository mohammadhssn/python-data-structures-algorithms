"""
Stack: Sort Stack (⚡Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack.  The function should use the pop, push, peek, and is_empty methods of the Stack object.

Note: This is a new function, not a method within the Stack class.

This will use the Stack class we created in these coding exercises:
30, 31, 32


To sort the stack, you should create a new, empty stack to hold the sorted elements.  Then, while the original stack is not empty, you should remove the top element from the original stack and compare it to the top element of the sorted stack.  If the top element of the sorted stack is greater than the current element, you should move the top element of the sorted stack back to the original stack until the current element is in the correct position.  Finally, you should add the current element to the sorted stack.

Once all the elements have been sorted, you should copy the sorted elements from the sorted stack to the original stack in the correct order.

Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.
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
    

def sort_stack(stack: Stack) -> None:
    # Create a new stack to hold the sorted elements
    additional_stack = Stack()
 
    # While the original stack is not empty
    while not stack.is_empty():
        # Remove the top element from the original stack
        temp = stack.pop()
 
        # While the additional stack is not empty and 
        #the top element is greater than the current element
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            # Move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())

        # Add the current element to the additional stack
        additional_stack.push(temp)
 
    # Copy the sorted elements from the additional stack to the original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()


"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
