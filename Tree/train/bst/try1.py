class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left.data = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right.data is None:
                