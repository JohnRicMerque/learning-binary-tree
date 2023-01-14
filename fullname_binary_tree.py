from binary_tree import BinarySearchTreeNode, build_tree
                
fullname = ["J", "O", "H", "N", "R", "I", "C", "C", "A", "T", "A", "P", "A", "N", "G", "M", "E", "R", "Q", "U", "E"]
fullname_tree = build_tree(fullname)

print("Input :",fullname)
print("Min:",fullname_tree.find_min())
print("Max:",fullname_tree.find_max())
print("In order traversal:", fullname_tree.in_order_traversal())
print("Post order traversal:", fullname_tree.post_order_traversal())
print("Pre order traversal:", fullname_tree.pre_order_traversal())

fullname_tree.delete("J")
print("After deleting J ",fullname_tree.in_order_traversal())
