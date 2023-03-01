class bst:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        
        if self.data is None:
            self.data = data
        else:  
            if data < self.data:
                if self.left is None:
                    self.left = bst(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = bst(data)
                else:
                    self.right.insert(data)
    def search(self,data):
        if self.data == data:
            return "found it"

        if data < self.data:
            if self.left is not None:
                return self.left.search(data)
            else:
                return "not found"
        else:
            if self.right is not None:
                return self.right.search(data)
            else:
                return "not found"

    def preorder_traversel(self):
        # root left right
        print(self.data)
        if self.left:
            self.left.preorder_traversel()
        if self.right:
            self.right.preorder_traversel()
    def inorder_traversel(self):
        # left root right
        if self.left:
            self.left.inorder_traversel()
        print(self.data)
        if self.right:
            self.right.preorder_traversel()
    def postorder_traversel(self):
        if self.left:
            self.left.postorder_traversel()
        if self.right:
            self.right.postorder_traversel()
        print(self.data)
    def delete(self,data):
        if data < self.data:
            self.left = self.delete(self.left)
        elif data > self.data:
            self.right = self.delete(self.right)
                 
            

root = bst(10)
root.insert(5)
root.insert(3)
root.insert(1)
root.insert(2)


# print(root.search(1))
root.postorder_traversel()
# print(root.left.left.left.data)
