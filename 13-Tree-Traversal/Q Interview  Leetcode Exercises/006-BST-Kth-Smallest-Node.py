"""
Instructions: 
BST: Kth Smallest Node
Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.

The solution to this problem usually involves traversing the tree in-order (left, root, right) and keeping track of the number of nodes visited until you find the kth smallest element. There are two main approaches to doing this:

Iterative approach using a stack: This approach involves maintaining a stack of nodes that still need to be visited, starting with the leftmost node. At each step, you pop a node off the stack, decrement the kth smallest counter, and check whether you have found the kth smallest element. If you have not, you continue traversing the tree by moving to the right child of the current node.

Recursive approach: This approach involves recursively traversing the tree in-order and keeping track of the number of nodes visited until you find the kth smallest element. You can use a helper function that takes a node and a value of k as input, and recursively calls itself on the left and right children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.
"""


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # ---------------------------------------------
    def recursive_kth_smallest(self, k):
        # initialize the number of nodes visited to 0
        self.kth_smallest_count = 0
        # call the helper function with the root node and k
        return self.recursive_kth_smallest_helper(self.root, k)
 
    def recursive_kth_smallest_helper(self, node, k):
        if node is None:
            # if the current node is None, return None
            return None
 
        # recursively call the helper function on the left child of the node and store the result in left_result
        left_result = self.recursive_kth_smallest_helper(node.left, k)
        if left_result is not None:
            # if left_result is not None, return it
            return left_result
 
        # increment the number of nodes visited by 1
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            # if the kth smallest element is found, return the value of the current node
            return node.value
 
        # recursively call the helper function on the right child of the node and store the result in right_result
        right_result = self.recursive_kth_smallest_helper(node.right, k)
        if right_result is not None:
            # if right_result is not None, return it
            return right_result
 
        # if the kth smallest element is not found, return None
        return None
    
    # ---------------------------------------------
    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []    
        # start at the root of the tree      
        temp = self.root    
        
        while stack or temp:
            # traverse to the leftmost node
            while temp: 
                # add the node to the stack                
                stack.append(temp)      
                temp = temp.left
            
            # pop the last node added to the stack
            temp = stack.pop()           
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:                  
                return temp.value
            
            # move to the right child of the node
            temp = temp.right           
            
        # if k is greater than the number of nodes in the tree, return None
        return None 
    

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7
print('---------------------------------------')
print(bst.recursive_kth_smallest(1))  # Expected output: 2
print(bst.recursive_kth_smallest(3))  # Expected output: 4
print(bst.recursive_kth_smallest(6))  # Expected output: 7

"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7
    ---------------------------------------
    2
    4
    7
 """
