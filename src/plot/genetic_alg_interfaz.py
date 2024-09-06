import numpy as np
import math

from alg import Alg
from bounded_function import BoundedFunction

class Genetic_Algorithm(Alg):
    def __init__(self, pop_size=50, F=0.9, CR=0.8, max_generations=2000):
        super().__init__("Genetic Algorithm")
        self.pop_size = pop_size
        self.F = 0.9
        self.CR = CR

        self.lower_bounds = None
        self.upper_bounds = None

        self.population = None
        self.fitness = None

    def mutate(self, population, F):
        num_individuals = self.pop_size
        dimensions = 2
        mutants = np.zeros_like(population)

        for i in range(num_individuals):
            candidates = list(range(num_individuals))
            candidates.remove(i)
            idxs = np.random.choice(candidates, 3, replace=False)
            x1 = population[idxs[0]]
            x2 = population[idxs[1]]
            x3 = population[idxs[2]]
            mutants[i] = (x1[0] + F + (x2[0] - x3[0]), x1[1] + F + (x2[1] - x3[1]))  

        return mutants

    def crossover(self, population, mutants, CR):
        num_individuals = self.pop_size
        dimensions = 2
        trials = []

        for i in range(num_individuals):
            x = mutants[i][0] if np.random.rand() < CR or 0 == np.random.randint(0, dimensions) else population[i][0]
            y = mutants[i][1] if np.random.rand() < CR or 1 == np.random.randint(0, dimensions) else population[i][1]
            trials.append((x, y))

        return trials

    def select(self, objective_function, population, trials, fitness):
        new_population = [(0, 0) for _ in range(self.pop_size)]
        new_fitness = [0]*self.pop_size

        for i in range(len(population)):
            ev = objective_function(trials[i][0], trials[i][1])
            if fitness[i] > ev:
                new_population[i] = trials[i]
                new_fitness[i] = ev
            else:
                new_population[i] = population[i]
                new_fitness[i] = fitness[i]

        return new_population, new_fitness


    def get_points(self) -> list[tuple[float, float]]:
        return self.population
    
    def initialize_points(self):
        self.population = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(self.pop_size)
        ]
    
    def check_inside(self, el):
        x = el[0]
        y = el[1]
        if el[0] < self.x1_range[0]:
            x = self.x1_range[0]
        if el[0] > self.x1_range[1]:
            x = self.x1_range[1]
        if el[1] < self.x2_range[0]:
            y = self.x2_range[0]
        if el[1] > self.x2_range[1]:
            y = self.x2_range[1]
        return (x, y)

    def update_points(self, bf: BoundedFunction):
        if self.fitness == None:
            self.fitness = [bf(x) for x in self.population]
            self.best_value = min(self.fitness)
            self.best_pos = self.population[np.argmin(self.fitness)]
            return
        
        mutants = self.mutate(self.population, self.F)
        trials = self.crossover(self.population, mutants, self.CR)
        for i, el  in enumerate(trials):
            trials[i] = self.check_inside(el)
        population, fitness = self.select(bf.f, self.population, trials, self.fitness)
        self.population = population
        self.fitness = fitness
        current_min = min(self.fitness)
        if current_min < self.best_value:
            self.best_value = current_min
            self.best_pos = self.population[np.argmin(fitness)]