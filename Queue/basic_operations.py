class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enque(self,data):
        newnode = Node(data)
        if self.front is None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = self.rear.next


    def deque(self):
        print('deque',self.front.data)
        self.front = self.front.next



    def print(self):
        rear = self.front
        while rear is not None:
            print(rear.data)
            rear = rear.next

if __name__ == "__main__":
    obj =  Queue()
    obj.enque(3)
    obj.enque(5)
    obj.enque(2)
    obj.enque(6)
    obj.print()
    obj.deque()
    obj.deque()
    obj.print()

