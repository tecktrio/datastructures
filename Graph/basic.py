class GRAPH:
    def __init__(self,nodes,is_directed = False) -> None:
        self.nodes = nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in nodes:
            self.adj_list[node] = []
    def degree(self,vertex):
        return len(self.adj_list[vertex])
    def print(self):
        print('created ',self.adj_list)
    def add(self,vertex_from,vertex_to):
        self.adj_list[vertex_from].append(vertex_to)
        if not self.is_directed:
            self.adj_list[vertex_to].append(vertex_from)
        

nodes = ['a','b','c','d']

graph = GRAPH(nodes,is_directed=True)
graph.add('a','b')
graph.add('a','c')
graph.print()
print(graph.degree('a'))