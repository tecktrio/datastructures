class Heap:
    def __init__(self) -> None:
        self.heap = []
    def insert(self,data):
        self.heap.append(data)
        self.fitit(len(self.heap) -1)

    def fitit(self,index):
        while index > 0 and self.heap[index] > self.heap[(index - 1)//2] : 
            self.heap[index] , self.heap[(index - 1)//2] = self.heap[(index - 1)//2], self.heap[index] 
            index = (index -1 )//2
    def remove(self):
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        index =0
        left = (index *2)+1
        right = (index *2)+2
        while left < len(self.heap):
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                max_index = right
            else:
                max_index = left
            if self.heap[max_index]  > self.heap[index]:
                self.heap[max_index],self.heap[index] = self.heap[index],self.heap[max_index]

            else:
                break

        return root
            
        

    def print(self):
        print(self.heap)

    def find_3_largest(self):
        t1 = self.remove()
        t2 = self.remove()
        t3 = self.remove()
        # t4 = self.remove()
        # t5 = self.remove()
        print(f'third largest number is {t3}')


heap = Heap()
heap.insert(10)
heap.insert(6)
heap.insert(3)
heap.insert(2)
heap.insert(7)

heap.find_3_largest()
# heap.print()