class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        print(self.peak())
        self.pop()
    def peak(self):
        return self.stack[len(self.stack) - 1]
    def print(self):
        for i in range(len(self.stack)):
            print(self.stack.pop())
            

obj = Stack()

string = "hello"
for char in string:
    obj.push(char)

obj.print()