class BinarySearchTreeNode:
    # defining binary search tree node class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data: # if the value already exists 
            return # then no need to add anything because binary search tree cannot have duplicate elements, hence return only
        
        if data < self.data: # if the value is less than the value of current node
            # add data in left subtree
            if self.left: # if left element has value
                self.left.add_child(data) # call the add_child method of that value that will lead to a recursion
            else: # if empty
                self.left = BinarySearchTreeNode(data) # assign data to the left subtree

        else: # if data is greater
            # add data in the right subtree
            if self.right: # if right element has value
                self.right.add_child(data) # call the add_child method of that value that will lead to a recursion
            else: # if empty
                self.right = BinarySearchTreeNode(data) # assign data to the right subtree
    
    def in_order_traversal(self): # return list of elements in the binary tree in order, left first, node then right
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal() # initiates a recursion, calling same function itself until it reaches the node, appends that to the list starting with left, base then right 

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0]) # instantiate class using array elements as argument

    for i in range(1, len(elements)):
        root.add_child(elements[i]) # loop through all array elements
    
    return root

if __name__ == '__main__': # note: this condition allows execution of code when file runs as a script, and not when imported as a module. This condition returns true whenever file is run as a script.
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]