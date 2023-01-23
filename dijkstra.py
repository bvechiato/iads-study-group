import math
from queue import PriorityQueue


class Vertex:
    def __init__(self, node: int):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.d = None
        self.pi = None
        self.Q = None

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node: int):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n: int):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(to, cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    # djikstra's
    def initialise_single_source(self, s):
        self.d = list(range(self.num_vertices))
        self.pi = list(range(self.num_vertices))
        for node_index in range(self.num_vertices):
            self.d[node_index] = math.inf
            self.pi[node_index] = None
        self.d[s] = 0

    def relax(self, u: int, v: int):
        print("Called relax")
        if self.d[v] == math.inf:
            self.d[v] = self.d[u] + self.get_vertex(u).get_weight(v)
            self.pi[v] = u
            self.Q.put((self.d[v], v))
        elif self.d[v] > self.d[u] + self.get_vertex(u).get_weight(v):
            self.d[v] = self.d[u] + self.get_vertex(u).get_weight(v)
            self.pi[v] = u
            self.Q.decrease_key(self.d[v], v)

    def dijkstra(self, s: int):
        self.initialise_single_source(s)
        self.Q = PriorityQueue()
        self.Q.put((0, s))
        while not self.Q.empty():
            d_star, u = self.Q.get()
            for key in self.vert_dict[u].adjacent:
                self.relax(u, key)
        print(f"d: {self.d}")


# self.pi for predecessors
g = Graph()

g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)

g.add_edge(0, 1, 7)
g.add_edge(0, 3, 9)
g.add_edge(0, 5, 14)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 11)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, 6)
g.add_edge(4, 5, 9)

g.dijkstra(0)

q = PriorityQueue()
q.put((4, 'a'))
q.decrease_key(0, 'a')
print(q.queue)

