class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        newnode = Node(data)
        if self.top is None:
            self.top = newnode
        else:
           newnode.next = self.top
           self.top = newnode
    def pop(self):
        if self.top is None:
            print('stack is empty')
        else:
            print(self.top.data)
            self.top = self.top.next
    def isEmpty(self):
        return self.top is None
    def print(self):
        if self.top is None:
            print('the stack is empty')
        else:
            top = self.top
            while top is not None:
                print(top.data)
                top  = top.next

    

