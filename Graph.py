import abc
from queue import Queue
import numpy as np


class Graph(abc.ABC):
    """The base class representation of graph with all the interface methods"""
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_wight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

    def breadth_first(self, fun=lambda x: print("visited : ", x), start=0):
        """It is a way of vising all the nodes in a graph, starting from start then visits all the adjacent nodes
        invoking every time the fun function"""
        queue = Queue()
        queue.put(start)
        visited = np.zeros(self.num_vertices)

        while not queue.empty():
            vertex = queue.get()
            if visited[vertex] == 1:
                continue
            fun(vertex)
            visited[vertex] = 1
            for v in self.get_adjacent_vertices(vertex):
                if visited[v] != 1:
                    queue.put(v)

    def depth_first(self, visited, fun=lambda x: print("visited : ", x), current=0):
        """It is a way of vising all the nodes in a graph, starting from start then goes in depth from that node
        until getting to a visited one, visited is a data structure for tilling visited nodes, 
        ex: np.zeros(self.num_vertices);  invoking every time the fun function"""
        if visited[current] == 1:
            return

        visited[current] = 1
        fun(current)
        
        for v in self.get_adjacent_vertices(current):
            self.depth_first(visited, fun, v)


def topological_sort(graph):
    """This function returns the topological sort of the graph as a list
    Important: We can do the topological sort of Directed Acyclic Graphs"""

    if not graph.directed:
        raise ValueError("It must be a Directed Acyclic Graphs")

    queue = Queue()
    indegree_map = {}
    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree()

        if indegree_map[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():
        vertex = queue.get()
        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] -= 1
            if indegree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This graph has a cycle")

    return sorted_list
