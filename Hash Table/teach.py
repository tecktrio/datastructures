class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None] * size
    def hashfunction(self,key):
        return key%self.size
    def insert(self,key,data):
        index = self.hashfunction(key)
        self.table[index] = data
    def delete(self,key):
        index = self.hashfunction(key)
        self.table[index] = None
    def search(self,key):
        index = self.hashfunction(key)
        return self.table[index]

obj = HashTable(10)
obj.insert(3,'amal')
obj.insert(4,'akhil')
obj.insert(5,'appu')
obj.insert(6,'gokul')
# obj.delete(5)
print(obj.search(5))

