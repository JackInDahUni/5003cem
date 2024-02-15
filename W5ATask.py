
""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

##########################################################################################

    
    def find_i(self, target):                   # This function searches for a target value in a binary search tree using an iterative approach
        cur_node = self.root                    # Start from the root node of the tree
        while cur_node is not None:             # Iterate until we reach a leaf node (None)
            if cur_node.data == target:         # If the current node's data is equal to the target, return True
                return True
            elif cur_node.data < target:        # If the target is less than the current node's data, move to the left child
                cur_node = cur_node.left
            else:                               # If the target is greater than the current node's data, move to the right child
                cur_node = cur_node.right
        return False                            # If the target is not found in the tree, return False

    
    def find_r(self, target):                   # This function serves as a wrapper for the recursive find operation
        if self.root:                           # It checks if the tree is not empty and calls the recursive find function
            if self._find_r(target, self.root): # If the tree is not empty, call the recursive find function
                return True
            return False                        # If the target is not found, return False
        else:
            return None                         # If the tree is empty, return None

    def _find_r(self, target, cur_node):        # This function recursively searches for a target value in a binary search tree
        if target > cur_node.data and cur_node.right:           # If the target is greater than the current node's data and the right child exists, recursively search in the right subtree
            return self._find_r(target, cur_node.right)
        elif target < cur_node.data and cur_node.left:          # If the target is less than the current node's data and the left child exists, recursively search in the left subtree
            return self._find_r(target, cur_node.left)
        if target == cur_node.data:                             # If the target is equal to the current node's data, return True
            return True


##########################################################################################
	
    
    def remove(self, target):                                               # This function searches for a target value removes it from the tree
        if self.root is None:                                               # Check if the tree is empty
            return False

        elif self.root.data == target:                                      # Check if the target is the root node
            if self.root.left is None and self.root.right is None:          # Case 1: Root node has no children
                self.root = None

            elif self.root.left and self.root.right is None:                # Case 2: Root node has only one child (either left or right)
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right

            else:                                                           # Case 3: Root node has both left and right children
                self.leftNRight(self.root)
            return True                                                     # Return after handling root removal

        parent = None
        node = self.root

        while node and node.data != target:                                 # Find the target node to be removed
            parent = node
            if target < node.data:
                node = node.left
            else:
                node = node.right

        if node is None or node.data != target:                             # If the target node is not found
            return False

        if node.left is None and node.right is None:                        # Case 1: Target node has no children
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None

        elif node.left and node.right is None:                              # Case 2: Target node has only one child (either left or right)
            if target < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
        elif node.left is None and node.right:
            if target < parent.data:
                parent.right = node.right
            else:
                parent.left = node.right

        else:                                                               # Case 3: Target node has both left and right children
            self.leftNRight(node)
        return True

    def leftNRight(self, node):
        delNodeParent = node
        delNode = node.right

        while delNode.left:                                                 # Find the minimum value in the right subtree
            delNodeParent = delNode
            delNode = delNode.left

        node.data = delNode.data                                            # Replace the value of the node to be removed with the value of the delete node

        if delNode == delNodeParent.right:                                  # Remove the delete node
            delNodeParent.right = delNode.right                             # Has at most one right child
        else:
            delNodeParent.left = delNode.right
    
##########################################################################################


#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)

bst.display(bst.root)

print("itterative: ", bst.find_i(1000))
print("recursive: ", bst.find_r(15))
bst.remove(2)
bst.display(bst.root)