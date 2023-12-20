"""
Instructions: 
Bubble Sort of LL (⚡Interview Question)
Assignment:

Write a bubble_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the bubble sort algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



Input:

The LinkedList object containing a linked list with unsorted elements (self).



Output:

None. The method sorts the linked list in place.



Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.

The bubble sort algorithm works by repeatedly iterating through the unsorted part of the list, comparing adjacent elements and swapping them if they are in the wrong order.

The method starts with the entire linked list being the unsorted part of the list.

For each pass through the unsorted part of the list, the method iterates through each pair of adjacent elements and swaps them if they are in the wrong order.

After each pass, the largest element in the unsorted part of the list will "bubble up" to the end of the list.

The method continues iterating through the unsorted part of the list until no swaps are made during a pass.

After the linked list is fully sorted, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.



Constraints:

The linked list can contain duplicates.

The method should be implemented in the LinkedList class.

The method should not use any additional data structures to sort the linked list.
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

    def bubble_sort(self) -> None:
        # Check if the list has less than 2 elements
        if self.length < 2:
            return
        
        # Initialize the sorted_until pointer to None
        sorted_until = None
        
        # Continue sorting until sorted_until reaches the second node
        while sorted_until != self.head.next:
            # Initialize current pointer to head of the list
            current = self.head
            
            # Iterate through unsorted portion of the list until sorted_until
            while current.next != sorted_until:
                next_node = current.next
                
                # Swap current and next_node values if current is greater
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                
                # Move current pointer to next node
                current = current.next
            
            # Update sorted_until pointer to the last node processed
            sorted_until = current
        
        # Update tail pointer to last node processed (i.e. largest element)
        self.tail = current


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
