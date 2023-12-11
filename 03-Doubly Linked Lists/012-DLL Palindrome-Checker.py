from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value: Any) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value: Any) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> None | Node:
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> None | Node:
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index: int) -> None | Node:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index: int, value: Any) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index: int, value: Any) -> bool:
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index - 1)
            after = before.next

            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node
        
        self.length += 1
        return True
    
    def remove(self, index: int) -> None | Node:
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def swap_first_last(self) -> None:
        if self.head is None or self.head == self.tail:
            return None
        self.head.value, self.tail.value = self.tail.value, self.head.value

    def reverse(self) -> None:
        temp = self.head
        while temp is not None:
            # swap the prev and next pointers of node points to
            temp.prev, temp.next = temp.next, temp.prev

            # move to the next node
            temp = temp.prev

        # swap the head and tail pointers
        self.head, self.tail = self.tail, self.tail

    def is_palindrome(self) -> bool:
        # If the length of the list is 0 or 1, it is always a palindrome
        if self.length <= 1:
            return True
        
        # Create two pointers, one starting from the head and the other from the tail
        forward_node = self.head
        backward_node = self.tail
        
        # Iterate over half of the list
        for i in range(self.length // 2):
            # If the values at the two ends of the list do not match, the list is not a palindrome
            if forward_node.value != backward_node.value:
                return False
            
            # Move the two pointers towards each other
            forward_node = forward_node.next
            backward_node = backward_node.prev
        
        # If all values matched, the list is a palindrome
        return True


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

print(my_doubly_linked_list.is_palindrome())  # True
