from random import uniform
from threading import Thread
from alg import Alg
from bounded_function import BoundedFunction

def _triangular(j, n):
    return 2 * (n + 1 - j) / n * (n + 1)

def _get_next_position(best : list[float], worst : list[float], S : float):
    next_position : list[float] = []

    for i in range(len(best)):
        difference = best[i] - worst[i]

        if difference >= 0:
            step = min(uniform(0, 1) * difference, S)
        else:
            step = max(uniform(0, 1) * difference, -S)

        next_position.append(worst[i] + step)

    return next_position

def _is_feasible(position : list[float], bounds : tuple[float, float]) -> bool:
    for value in position:
        if not(bounds[0] <= value <= bounds[1]):
            return False;
    return True

def _evolve_builder(objective_function, q : int, N : int, S : float, bounds : tuple[float, float]):
    def evolve(memeplexes : dict[int, list[list[float]]], index : int, memeplex : list[list[float]], global_best : list[float]):
        for _ in range(N):
            # Step 1: Construct submemeplex
            memeplex = sorted(memeplex, key=lambda frog: objective_function(frog)) # Sort by fitness
            memeplex = sorted(memeplex, key=lambda frog: -_triangular(memeplex.index(frog), len(memeplex))) # Sort by triangular probability distribution
            submemeplex = memeplex[:q] # Take subset of size q
            submemeplex = sorted(submemeplex, key=lambda frog: objective_function(frog)) # Sort by fitness

            # Step 2: Improve worst frog's position
            local_best = submemeplex[0]
            local_worst = submemeplex[len(submemeplex) - 1]

            next_position = _get_next_position(local_best, local_worst, S)

            if _is_feasible(next_position, bounds) and objective_function(next_position) < objective_function(local_worst):
                submemeplex[len(submemeplex) - 1] = next_position
                memeplex[0:q] = submemeplex
                continue
            
            # Step 3: Try to improve using the global best frog
            next_position = _get_next_position(global_best, local_worst, S)

            if _is_feasible(next_position, bounds) and objective_function(next_position) < objective_function(local_worst):
                submemeplex[len(submemeplex) - 1] = next_position
                memeplex[0:q] = submemeplex
                continue

            # Step 6 (Censorship): Stop spread of defective meme and generate a new random positioned frog
            submemeplex[len(submemeplex) - 1] = [uniform(bounds[0], bounds[1]) for _ in range(len(global_best))]
            memeplex[0:q] = submemeplex

        memeplexes[index] = memeplex
            
    return evolve

class SFLA(Alg):
    '''
    Shuffled frog leaping algorithm. A memetic meta-heuristic algorithm for function optimization.

    Constructor parameters
    ----------
    objective_function : function
        Objective function.
    m : int 
        Number of memeplexes (partitions of the population).
    n : int 
        Number of frogs per memeplex.
    dimension : int 
        Number of variables in the objective function (known as meme-size).
    N : int 
        Number of iterations per memeplex.
    q : int
        Size of memeplexes.
    S : float 
        Maximum step-size when improving worst local frog position.
    bounds : tuple[float, float]
        Objective functions's variables bounds
    '''
    def __init__(self, name: str, objective_function, m : int, n : int, dimension : int, N : int, q : int, S : float, bounds : tuple[float, float] = (-100, 100)):
        super().__init__(name)
        self.objective_function = lambda X: objective_function(X[0], X[1])
        self.m = m
        self.n = n
        self.dimension = dimension
        self.N = N
        self.q = q
        self.bounds = bounds
        self.evolve = _evolve_builder(self.objective_function, q, N, S, bounds)

        F = m * n # Population size
        self.population : list[list[float]] = []

        # Step 1: Generate virtual frogs population
        for _ in range(F):
            frog = [uniform(bounds[0], bounds[1]) for _ in range(dimension)]
            self.population.append(frog)

        # Step 2: Rank frogs
        self.population = sorted(self.population, key = lambda frog: self.objective_function(frog))
        self.global_best = self.population[0]

    def get_points(self):
        return self.population

    def update_points(self, bf: BoundedFunction):
        # Step 3: Partition frogs into memeplexes
        memeplexes : dict[int, list[list[float]]] = {}

        for i, frog in enumerate(self.population):
            index = i % self.m
            if index not in memeplexes:
                memeplexes[index] = [frog]
            else:
                memeplexes[index].append(frog)

        # Step 4: Memetic evolution with each memeplex
        threads : list[Thread] = []
        for memeplex in memeplexes.values():
            thread = Thread(target=self.evolve(memeplexes, index, memeplex, self.global_best))
            threads.append(thread)
            thread.start()
            # self.evolve(memeplexes, index, memeplex, self.global_best)

        for thread in threads:
            thread.join()

        # Step 5: Shuffle memeplexes
        self.population = []
        for memeplex in memeplexes.values():
            self.population += memeplex

        self.population = sorted(self.population, key= lambda frog: self.objective_function(frog))

        self.global_best = self.population[0]
        self.best_pos = self.global_best