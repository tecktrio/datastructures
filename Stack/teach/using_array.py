class Stack:
    def __init__(self):
        self.arr = []
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        self.arr.pop()
    def print(self):
        for i in range(len(self.arr)):
            print(self.arr[i])


obj = Stack()
obj.push(2)
obj.push(1)
obj.push(3)
obj.push(4)
obj.push(5)
obj.pop()
obj.print()
