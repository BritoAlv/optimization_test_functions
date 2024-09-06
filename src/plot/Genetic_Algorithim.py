import numpy as np
import math

def mutate(population, F):
    num_individuals, dimensions = population.shape
    mutants = np.zeros_like(population)

    for i in range(num_individuals):
        candidates = list(range(num_individuals))
        candidates.remove(i)
        idxs = np.random.choice(candidates, 3, replace=False)
        x1, x2, x3 = population[idxs]
        mutant = x1 + F * (x2 - x3)
        mutants[i] = mutant

    return mutants

def crossover(population, mutants, CR):
    num_individuals, dimensions = population.shape
    trials = np.zeros_like(population)

    for i in range(num_individuals):
        for j in range(dimensions):
            if np.random.rand() < CR or j == np.random.randint(0, dimensions):
                trials[i, j] = mutants[i, j]
            else:
                trials[i, j] = population[i, j]

    return trials

def select(objective_function, population, trials, fitness):
    new_population = np.zeros_like(population)
    new_fitness = np.zeros_like(fitness)

    for i in range(len(population)):
        if fitness[i] > objective_function(trials[i]):
            new_population[i] = trials[i]
            new_fitness[i] = objective_function(trials[i])
        else:
            new_population[i] = population[i]
            new_fitness[i] = fitness[i]

    return new_population, new_fitness

def differential_evolution(objective_function, bounds, pop_size=50, F=0.9, CR=0.8, max_generations=2000):
    dimensions = len(bounds)
    population = np.random.rand(pop_size, dimensions)
    
    lower_bounds, upper_bounds = np.array(bounds).T
    diff = np.fabs(lower_bounds - upper_bounds)
    population = lower_bounds + population * diff

    fitness = np.array([objective_function(ind) for ind in population])

    for generation in range(max_generations):
        mutants = mutate(population, F)
        trials = crossover(population, mutants, CR)
        trials = np.clip(trials, lower_bounds, upper_bounds)
        population, fitness = select(objective_function, population, trials, fitness)

        best_idx = np.argmin(fitness)
        #print(f"Generación {generation + 1}: Mejor valor de la función objetivo = {fitness[best_idx]}")

        if fitness[best_idx] < 1e-8:
            break

    return population[best_idx], fitness[best_idx]


#print("Mejor solución encontrada:", result[0])
#print("Valor de la función objetivo en la mejor solución:", result[1])


