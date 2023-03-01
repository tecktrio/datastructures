class Node:
    def __init__(self) -> None:
        self.children = {}
        self.endofWord = False
class Trie:
    def __init__(self) -> None:
        self.root = Node()
    def insert(self,data):
        cur = self.root
        for c in data:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endofWord = True
    
    def search(self,data):
        cur = self.root
        for c in data:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.endofWord:
            return True
        return False
    def startswith(self,data):
        cur = self.root
        for c in data:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
trie= Trie()
trie.insert('amal')
trie.insert('akhil')
trie.insert('aklikuttan')
trie.insert('benny')
trie.insert('beena')

while True:
    data = input('')
    print(trie.startswith(data))
            