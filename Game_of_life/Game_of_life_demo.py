# -*- coding: utf-8 -*-
"""
Game of life
"""


import tkinter as tk
import numpy as np
import copy


class GameOfLife:
    def __init__(self, space_size, initial_possibility, iterate_number):
        self.size = space_size
        self.initial_possibility = initial_possibility
        self.iterate_number = iterate_number
        self.convolution = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        self.round = 0

        """
        Args:
            size: size of living space [maybe 10 or 20 ...]
            initial_possibility: defining initial life intensity 【from 0 to 1】
            iterate_number: total numbers of iteration   [100 or 200]
            convolution: convolution to calculate the lives of one cell [matrix]
            round: number of this iteration
        """

    def life_evolution(self):
        # Initialize this game
        initial_state = np.random.random((self.size, self.size))
        initial_state[initial_state < self.initial_possibility] = 0
        initial_state[initial_state > self.initial_possibility] = 1

        # append lifeless space around initial space in order to use convolution directly
        append_raw = np.zeros((1, self.size))
        append_col = np.zeros((self.size + 2, 1))
        initial_state = np.r_[initial_state, append_raw]
        initial_state = np.r_[append_raw, initial_state]
        initial_state = np.c_[initial_state, append_col]
        initial_state = np.c_[append_col, initial_state]
        state = copy.copy(initial_state)

        # start iterate
        for i in range(self.iterate_number):
            life_position = []  # record the location of life
            for raw in range(1, self.size + 1):
                for col in range(1, self.size + 1):
                    one_cell = initial_state[raw - 1: raw + 2, col - 1: col + 2]
                    neighbor_number = (one_cell * self.convolution).sum()
                    if neighbor_number == 3:
                        state[raw, col] = 1.0
                        life_position.append([raw, col])
                    elif neighbor_number == 2:
                        state[raw, col] = initial_state[raw, col]
                        if state[raw, col] == 1:
                            life_position.append([raw, col])
                    else:
                        state[raw, col] = 0
            initial_state = copy.copy(state)
            self.round += 1
            if self.round % 5 == 0:
                self.show_distribution(life_position)

    def show_distribution(self, life_position):
        window = tk.Tk()
        window.title('Game Of Life' + str(self.round))
        window.geometry('800x800')
        for i in range(self.size):
            for j in range(self.size):
                tk.Label(window, background='white', relief='sunken').\
                    grid(row=i, column=j, padx=0, pady=0, ipadx=10, ipady=2)
        for position in life_position:
            tk.Label(window, background='black').grid(row=position[0] - 1, column=position[1] - 1, ipadx=10, ipady=2)
        window.mainloop(5)


if __name__ == '__main__':
    GameOfLife(20, 0.4, 100).life_evolution()
