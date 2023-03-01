class Heap:
    HEAP_SIZE = 10
    def __init__(self) -> None:
        self.heap = []

    def insert(self,data):
        self.heap.append(data)
        index = len(self.heap)-1
        self.fixUp(index)
    def fixUp(self,index):

        while index > 0 and self.heap[index] < self.heap[(index-1)//2]:
            self.heap[(index-1)//2], self.heap[index] = self.heap[index], self.heap[(index-1)//2]
            index = (index-1)//2

    def delete(self):
        root = self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()

        # start heapyfing
        print(self.heap)
        self.heapify(self.heap,0)
        return root
        
    def heapify(self,heap,index):

        right = (index * 2)+ 2
        left = (index * 2)+ 1
        min_index= 0 
        if right < len(heap) and heap[right] < heap[left]:
            min_index = right
        elif left < len(heap):
            min_index = left
        if heap[min_index] < heap[index]:
            heap[min_index],heap[index] = heap[index],heap[min_index]
            self.heapify(heap,min_index)
        return
   


heap = Heap()
heap.insert(10)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(9)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(1)

print('root',heap.delete())

print('root',heap.delete())


print(heap.heap)