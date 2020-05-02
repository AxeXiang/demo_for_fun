# -*- coding: utf-8 -*-
"""
Try some methods for finding shortest path between nodes in a graph
"""
import numpy as np
import random
import math


class FindShortestPath:
    def __init__(self, map_matrix, start_point):
        self.map_matrix = map_matrix
        self.node_number = map_matrix.shape[0]
        self.start_point = start_point
        self.distance = np.ones(self.node_number) * np.inf

    def Dijkstra(self):
        for j in range(self.node_number):
            self.distance[j] = self.map_matrix[self.start_point][j]
            for k in range(self.map_matrix.shape[0]):
                if self.map_matrix[self.start_point][k] + self.map_matrix[k][j] < self.map_matrix[self.start_point][j]:
                    self.distance[j] = self.map_matrix[self.start_point][k] + self.map_matrix[k][j]
        print(self.distance)


if __name__ == '__main__':
    # Generate initial map
    matrix = np.random.randint(1, 9, 36).reshape(6, 6)
    matrix = np.triu(matrix)
    matrix[2][3] = 1000
    matrix[4][5] = 1000
    for i in range(matrix.shape[0]):
        matrix[i][i] = 0
    matrix += matrix.T - np.diag(matrix.diagonal())
    print(matrix)
    start_point = random.randint(0, matrix.shape[0] - 1)
    point_dict = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F"}
    print("Start Point" + ":" + "\t" + "{" + point_dict[str(start_point)] + "}")
    FindShortestPath(matrix, start_point).Dijkstra()
