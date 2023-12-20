"""
to be in ascending order, but the input lists themselves do not need to be sorted.

Parameters

other_list (LinkedList): the other LinkedList to merge with the current list



Return Value

This method does not return a value, but it modifies the current LinkedList to contain the merged list.



Example:

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)
 
l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)
 
l1.merge(l2)
 
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]


Details

The merge method works as follows:

It gets the head node of the other linked list (other_list.head) and sets it to a local variable called other_head.

It creates a new node called dummy with a value of 0, which will serve as the head of the merged linked list.

It creates a new node called current and sets it equal to `

"""


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list: 'LinkedList') -> None:
        # Get the head node of the other linked list
        other_head = other_list.head
        
        # Create a dummy node to hold the merged list
        dummy = Node(0)
        
        # Set the current node to the dummy node
        current = dummy
    
        # Loop while both lists still have nodes
        while self.head is not None and other_head is not None:
            
            # Compare the values of the first nodes in each list
            if self.head.value < other_head.value:
                # If the value in the first list is smaller,
                # add it to the current node and move to the next node in the first list
                current.next = self.head
                self.head = self.head.next
            else:
                # Otherwise, add the value from the second list
                # and move to the next node in the second list
                current.next = other_head
                other_head = other_head.next
                
            # Move the current node to the next position
            current = current.next
    
        # If the first list still has nodes left, add them to the current node
        if self.head is not None:
            current.next = self.head
        else:
            # If the second list still has nodes left, add them to the current node
            current.next = other_head
            # Update the tail of the merged list to be the tail of the second list
            self.tail = other_list.tail
    
        # Set the head of the merged list to the next node after the dummy node
        self.head = dummy.next
        
        # Update the length of the merged list
        self.length += other_list.length
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
