

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else: self.right.insert(data)

        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.data)

        if self.right:
            self.right.printTree()

    def height(self):
        lh,rh = 0,0
        if self.data is None:
            return 0
        if self.left:
            lh = self.left.height()
        if self.right:
            rh = self.right.height()

        return 1 + max(lh, rh)

root = TreeNode(9)
root.insert(11)
root.insert(7)
root.insert(6)
root.insert(10)
root.insert(12)
root.insert(5)
root.insert(8)
root.insert(7)
# root.printTree()
print(root.height())


