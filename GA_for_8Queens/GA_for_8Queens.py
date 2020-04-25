# -*- coding: utf-8 -*-
"""
Genetic Algorithm to solve 8 Queens problem
unfinished, to be continue...
"""

import numpy as np


class GA8Queen:
    def __init__(self, queen_number, pop_size, cross_rate, mutate_rate):
        self.queen_number = queen_number
        self.pop_size = pop_size
        self.cross_rate = cross_rate
        self.mutate_rate = mutate_rate
        self.pop = np.vstack([np.random.permutation(queen_number) for _ in range(pop_size)])
        self.all_state = []

    def get_fitness(self, queen_state):
        # get fitness according to the rule
        fitness = 0
        for i in set(queen_state):
            if queen_state.tolist().count(i) > 1:
                fitness += (queen_state.tolist().count(i) - 1)
        for i in range(len(queen_state)):
            for j in range(len(queen_state)):
                if j > i:
                    if abs(queen_state[j] - queen_state[i]) == abs(j - i):
                        fitness += 1
        return fitness

    def tournament(self, tournament_size):
        # use tournament method to find the fittest state from a sub-population
        all_parent = []
        all_fitness = []
        for i in range(self.pop_size):
            contenders = np.random.randint(0, self.pop_size, tournament_size)
            fitness = [self.get_fitness(self.pop[x]) for x in contenders]
            parent_index = contenders[np.argmin(fitness)]
            parent = self.pop[parent_index]
            parent_fitness = np.min(fitness)
            all_parent.append(parent)
            all_fitness.append(parent_fitness)
        return all_parent, all_fitness

    def evolve(self, tournament_size):
        pop, fitness = self.tournament(tournament_size)
        if 0 in fitness:
            position = fitness.index(0)
            self.all_state.append(pop[position])

        pop_copy = pop.copy()



if __name__ == '__main__':
    GA8Queen(queen_number=8, pop_size=100, cross_rate=0.4, mutate_rate=0.2).evolve(20)
