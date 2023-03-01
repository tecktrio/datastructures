class Node:
    def __init__(self) -> None:
        self.childrens = {}
        self.endofword = False

class trie:
    def __init__(self) -> None:
        self.root = Node()
    def insert(self,word):
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur.childrens[ch] = trie()
            cur = cur.childrens[ch]
        cur.endofword = True

    