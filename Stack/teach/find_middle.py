
def find_middle(stack):
    stack1 = []
    stack2 = []

    while len(stack) > 0:
        print(stack[-1])
        stack1.append(stack.pop())
        if len(stack) > 0:
            print(stack[-1])
            stack2.append(stack.pop())
    if len(stack1) > len(stack2):
        return stack1[-1]
    else:
        return stack2[-1]



 
arr = [3,5,2,3,1,6]
print(find_middle([1,2,3,4,5,6,7,8,9]))