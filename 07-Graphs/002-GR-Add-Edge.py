class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self) -> None:
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex: str) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1: str, v2: str) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    

my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""
