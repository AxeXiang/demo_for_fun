# -*- coding: utf-8 -*-
"""
Try some methods for finding shortest path between nodes in a graph
"""
import numpy as np
import random


class FindShortestPath:
    def __init__(self, map_matrix):
        self.map_matrix = map_matrix
        self.node_number = map_matrix.shape[0]

    def Dijkstra(self):
        for i in range(self.node_number):
            for j in range(self.node_number):
                for k in range(self.node_number):
                    if self.map_matrix[j, i] + self.map_matrix[i, k] < self.map_matrix[j, k]:
                        self.map_matrix[j, k] = self.map_matrix[j, i] + self.map_matrix[i, k]
                        self.Dijkstra()
        return self.map_matrix


if __name__ == '__main__':
    # Generate initial map
    matrix = np.random.randint(1, 9, 25).reshape(5, 5)
    matrix = np.triu(matrix)
    matrix[2][3] = 1000
    # matrix[3][4] = 1000
    for n in range(matrix.shape[0]):
        matrix[n][n] = 0
    matrix += matrix.T - np.diag(matrix.diagonal())
    print(matrix)
    start_point = random.randint(0, matrix.shape[0])
    point_dict = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F"}
    print("Start Point" + ":" + "\t" + "{" + point_dict[str(start_point)] + "}")
    final = FindShortestPath(matrix).Dijkstra()
    print(final)
