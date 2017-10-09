"""This is a simple library for the manipulation using Matrix
the Graph is a Matrix of [n*n]; n == the number of nodes
and at each intersection[v1,v2] is the weight of the connection from v1 to v2"""
from Graph import *
import numpy as np


class AdjacencyMatrixGraph(Graph):
    """Represents a graph as an adjacency matrix. A cell in the matrix has a value
     when there exists an edge between the vertex represented by the row and column
     numbers.
     Weighted graphs can hold values > 1 in the matrix cells
     A value of 0 in the cell indicates that there is no edge """

    def __init__(self, num_vertices, directed=False):
        super(self.__class__, self).__init__(num_vertices, directed)
        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("vertices %d or %d are out of range" % (v1, v2))

        if weight < 0:
            raise ValueError("An edge cannot be negative")

        self.matrix[v1][v2] = weight

        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("vertices %d are out of range" % v)

        return {_: self.matrix[v][_] for _ in range(self.num_vertices) if self.matrix[v][_] > 0}

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError("vertices %d are out of range" % v)

        i = 0
        for _ in self.matrix[v]:
            if _ > 0: i += 1
        return i

    def get_edge_wight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)

if __name__ == "__main__":
    a = AdjacencyMatrixGraph(5)
    a.add_edge(2, 3)
    a.add_edge(2, 4)
    a.add_edge(4, 3)
    a.add_edge(1, 0)
    a.add_edge(2, 0)
    a.display()