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
                self.left.add_child(data) # call the add_child method of that value 
            else: # if empty
                self.left = BinarySearchTreeNode(data) # assign data to the left subtree

        else: # if data is greater
            # add data in the right subtree
