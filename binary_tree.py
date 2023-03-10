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
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(val) # another recursion to search for val until reaches point where there is no value
            else:
                return False # then return false

        if val > self.data:
            # value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False # then return false
        
    def find_min(self): # finding minimum value by traversing the most left value 
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self): # finding minimum value by traversing the most right value
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data: 
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None: # means no child return none
                return None
            elif self.left is None: # one child
                return self.right
            elif self.right is None:
                return self.left

            # min_val = self.right.find_min() # used min value of the right subtree
            # self.data = min_val
            # self.right = self.right.delete(min_val) # delete duplicate node then return new right subtree

            # Another implementation of delete method for the exercise using max value of the left subtree

            max_val = self.left.find_max() # used max value of the left subtree
            self.data = max_val
            self.left = self.left.delete(max_val) # delete duplicate node then return new left subtree

        return self
    
    def calculate_sum(self): # traverses through the left and right tree and adds them together
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def post_order_traversal(self): # return list of elements in the binary tree in order, left first, right tree, then base node
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self): # return list of elements in the binary tree in order, base node first, left tree then right tree
        elements = [self.data] # base node first

        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
                

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0]) # instantiate class using array elements as argument

    for i in range(1, len(elements)):
        root.add_child(elements[i]) # loop through all array elements
    
    return root

if __name__ == '__main__': # note: this condition allows execution of code when file runs as a script, and not when imported as a module. This condition returns true whenever file is run as a script.

    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)

    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())
