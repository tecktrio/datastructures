#basic operaions of stack are: push, pop, peak, isempty, isfull

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
            return "your stack is empty"
        else:
            print(self.top.data)
            self.top  = self.top.next

    def peak(self):
        if self.top is None:
            return "stack is empty"
        else:
            return self.top.data
    def print(self):
        if self.top is None:
            return "stack is empty"
        else:
            tail = self.top
            while tail is not None:
                print(tail.data,end = ' => ')
                tail = tail.next


if __name__ == '__main__':
    obj = Stack()
    obj.push(2)
    obj.push(3)
    obj.push(5)
    obj.push(1)
    obj.print()
