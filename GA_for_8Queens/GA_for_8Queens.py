# -*- coding: utf-8 -*-
"""
Genetic Algorithm to solve 8 Queens problem
Obviously this is not an effective method,
I just try to solve it with genetic algorithm.
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
        all_parents = []
        all_fitness = []
        for i in range(self.pop_size):
            contenders = np.random.randint(0, self.pop_size, tournament_size)
            fitness = [self.get_fitness(self.pop[x]) for x in contenders]
            parent_index = contenders[np.argmin(fitness)]
            parent = self.pop[parent_index]
            parent_fitness = np.min(fitness)
            all_parents.append(parent)
            all_fitness.append(parent_fitness)
        return np.array(all_parents), np.array(all_fitness)

    def record_and_replace(self, all_parents, all_fitness):
        if 0 in all_fitness:
            zero_position = [i for i, v in enumerate(all_fitness) if v == 0]
            perfect_state = np.unique(all_parents[zero_position], axis=0).tolist()
            for one_state in perfect_state:
                if one_state not in self.all_state:
                    self.all_state.append(one_state)
            all_parents = np.delete(all_parents, zero_position, axis=0)
            add_pop = np.vstack([np.random.permutation(self.queen_number) for _ in range(len(zero_position))])
            all_parents = np.append(all_parents, add_pop, axis=0)
        return all_parents

    def crossover(self, parent, all_parents):
        if np.random.rand() < self.cross_rate:
            i_ = np.random.randint(0, self.pop_size, size=1)
            cross_points = np.random.randint(0, 2, self.queen_number).astype(np.bool)
            parent[cross_points] = all_parents[i_, cross_points]
        return parent

    def mutate(self, child):
        for point in range(self.queen_number):
            if np.random.rand() < self.mutate_rate:
                swap_point = np.random.randint(0, self.queen_number)
                swapA, swapB = child[point], child[swap_point]
                child[point], child[swap_point] = swapB, swapA
        return child

    def evolve(self, tournament_size, generation):
        for n in range(generation):
            all_parents, all_fitness = self.tournament(tournament_size)
            all_parents = self.record_and_replace(all_parents, all_fitness)
            all_parents_copy = all_parents.copy()
            for parent in all_parents:
                child = self.crossover(parent, all_parents_copy)
                child = self.mutate(child)
                parent[:] = child
            self.pop = all_parents
            print(self.all_state)
            print(len(self.all_state))


if __name__ == '__main__':
    GA8Queen(queen_number=6, pop_size=1000, cross_rate=0.1, mutate_rate=0.4).evolve(20, 200)
