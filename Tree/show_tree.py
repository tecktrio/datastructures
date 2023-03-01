class BST:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = BST(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BST(data)
                else:
                    self.right.insert(data)
    def search(self,data):
        # print(data,self.data)
        if data  == self.data:
            return True
        if data < self.data:
            if self.left is not None:
                if self.left.search(data):
                    return True
            return False
        elif data > self.data:
            if self.right is not None:
                if self.right.search(data):
                    return True
            return False
        else:
            return False

    def delete(self,root,data):
        if data == root.data:
            if not root.left:
                root = None
                return root.right
            if not root.right:
                root = None
                return root.left
            root.right = self.minvalue(root.right)
            root.right = self.delete(root.right,root.right.data)

        if data < root.data:
            self.left = self.delete(self.left,data)
        if data > root.data:
            self.right = self.delete(self.right,data)

    def minvalue(self,root):
        while root.left is not None:
            root = root.left

        return root


root = BST(5)
root.insert(1)
root.insert(2)
root.insert(6)
root.insert(4)
root.insert(5)
root.insert(3)

print(root.search(3))