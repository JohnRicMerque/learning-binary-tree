class BinarySearchTreeNode:
    # defining binary search tree node class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data: # if the value already exists 
            return # then no need to add anything because binary search tree cannot have duplicate elements, hence return only
        