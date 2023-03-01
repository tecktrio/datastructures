class Bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data is None:
            self.data == data
            return 
        if data < self.data:
            if self.left is None:
                self.left = Bst(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Bst(data)
            else:
                self.right.insert(data)
                
    def delete(self,root,data):
        if root is None:
            return "there is no data"

        if root.data == data:
            # if there the key is a leaf
            if root.left is None:
                return root.right.data
            if root.right is None:
                return root.left.data
            
            root.right = self.minvalue(root.right)
            root.right = self.delete(root.right,root.right.data)
            
        elif root.data < data:
            root.left = self.delete(root.left,data)
        elif root.data > data:
            root.right = self.delete(root.right,data)
        return root
    def minvalue(self,root):
        cur = root.left
        while cur is None:
            cur = cur.left
        return cur

    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
            print(self.data)
        if self.right:
            self.right.in_order_traversal()
    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)

root = Bst(2)
root.insert(1)
root.insert(4)
root.insert(5)
root.insert(3)
print(root.post_order_traversal())