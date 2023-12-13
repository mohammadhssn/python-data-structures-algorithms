from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node | None:
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> Node | None:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index: int) -> Node | None:
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True 

    def remove(self, index: int) -> Node | None:
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self) -> None:
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
    def find_middle(self) -> Node:
        # Initialize two pointers to the head of the list
        slow = self.head
        fast = self.head
        
        # Traverse the list with the fast pointer moving twice
        # as fast as the slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            
        # When the fast pointer reaches the end, the slow
        # pointer will be at the middle node
        return slow
    
    def has_loop(self) -> bool:
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def remove_duplicates(self) -> None:
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

    def find_kth_from_end(self, k: int) -> None | Node:
        # Initialize both slow and fast pointers to 
        # the head node of the linked list
        slow = fast = self.head   
        
        # Move the fast pointer k nodes ahead of the slow pointer
        # If fast pointer reaches the end (None) before k nodes, 
        # the linked list is too short and kth node doesn't exist
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
    
        # Move both pointers one node at a time until the fast 
        # pointer reaches the end of the linked list (None).
        # The slow pointer will now be pointing at the kth node 
        # from the end of the linked list.
        while fast:
            slow = slow.next
            fast = fast.next
            
        # Return the kth node from the end of the linked list
        return slow.value
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print(my_linked_list.find_kth_from_end(3))  # 2
