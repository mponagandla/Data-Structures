

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = Tree()
print("Please enter the left node value")
left_node = Tree(input())
print("Please enter the right node value")
right_node = Tree(input())
root.left = id(left_node)
root.right = id(right_node)

#print("Left node address : {}" % id(left_node) )
#print("Right node address : {}" % id(right_node) )
print("Root left node address : {}" % root.left )
print("Root right node address : {}" % root.right )
