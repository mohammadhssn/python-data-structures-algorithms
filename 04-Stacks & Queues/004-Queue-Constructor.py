from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value: Any) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self) -> None:
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_queue = Queue(4)

my_queue.print_queue()

"""
    EXPECTED OUTPUT:
    ----------------
    4
"""
