
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self):
        self.size = 5
        self.table = [None] * self.size

    def hash_function(self,key):
        return key % self.size

    def insert(self,key,value):
        index = self.hash_function(key)
        node = self.table[index]
        newnode = Node(key,value)
        if node is None:
            node = newnode
        else:
            while node is not None:
                node = node.

    def search(self,key):
        index = self.hash_function(key)
        return self.table[index]
        
    def delete(self,key):
        index = self.hash_function(key)
        for i in range(index,len(self.table)-1):
            self.table[i] = self.table[i+1]

    def lookup(self,key):
        index = self.hash_function(key)



