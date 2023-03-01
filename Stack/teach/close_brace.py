class Stack:
    def __init__(self):
        self.list = []
    def push(self,data):
        self.list.append(data)
    def pop(self):
        self.list.pop()
    def peak(self):
        return self.list[len(self.list)-1]
    def print(self):
        for i in self.list:
            print(i)

obj = Stack()
status = True
opening = ['{','(','[']
closing = ['}',')',']']
string = '({[]})'
input  = [ i for i in string]
print(input)

for i in input:
    if i in opening:
        obj.push(i)
    elif i in closing:
        pos = closing.index(i)
        if obj.peak() == opening[pos]:
            obj.pop()
        else:
            status = False
            break
if status == True:
    print('The braces are closed')
else:
    print('not closed')


    