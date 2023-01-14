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
