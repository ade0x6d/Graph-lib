"""This is a simple library for the manipulation of graphs using sets(key: the vertex ID but no weight)
the Graph is a list of Nodes and every Node have an ID and a set for all the connections"""
from Graph import *
from queue import Queue


class Node:
    """A single node in a graph represented by an adjacency set. Every node has a vertex id
    Each node is associated with a set of adjacent vertices"""

    def __init__(self, vertexID):
        self.vertexID = vertexID
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexID == v:
            raise ValueError("The vertex %d can't be adjacent to it self.")

        self.adjacency_set.add(v)

    def get_adjacency_set(self):
        return sorted(self.adjacency_set)  # sorted only for convenient


class AdjacencySetGraph(Graph):
    """Represents a graph as an adjacency set. A graph is a list of nodes and each node has a set of adjacent vertices.
    This in this current form cannot be used to represent Weighted edges only unweighted graphs can be represented """

    def __init__(self, num_vertices, directed=False):
        super(self.__class__, self).__init__(num_vertices, directed)

        self.vertex_list = []
        for _ in range(num_vertices):
            self.vertex_list.append(Node(_))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("vertices %d or %d are out of range" % (v1, v2))

        if weight != 1:
            raise ValueError("The wight must be 1")  # because it cannot represent weighted graphs

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("vertices %d are out of range" % v)

        return self.vertex_list[v].get_adjacency_set()

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("vertices %d are out of range" % v)

        i = 0
        for _ in range(self.num_vertices):
            if v in self.get_adjacent_vertices(_):
                i += 1

        return i

    def get_edge_wight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)


def build_distance_table(graph, source):
    """This function can be used only for unweighted graphs
    :return A dictionary mapping from the vertexID number to tuple of
    (distance from source, last vertex on path from source)"""
    distance_table = {i: (None, None) for i in range(graph.num_vertices)}
    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()
        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            if distance_table[neighbor][1] is None:
                distance_table[neighbor] = (1 + current_distance, current_vertex)

                if len(graph.get_adjacent_vertices(neighbor)):
                    queue.put(neighbor)

    return distance_table


def shortest_path(graph, source, destination):
    """This function can be used only for unweighted graphs
    :return The shortest path from source te destination; [] if doesn't exists"""
    distance_table = build_distance_table(graph, source)

    path = [destination]
    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        return []
    else:
        return [source] + path

if __name__ == "__main__":
    a = AdjacencySetGraph(5)
    a.add_edge(2, 3)
    a.add_edge(2, 4)
    a.add_edge(4, 3)
    a.add_edge(1, 0)
    a.add_edge(2, 0)
    a.display()
    print(shortest_path(a, 0, 4))
