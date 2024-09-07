import numpy as np
from plot.alg import Alg
from plot.bounded_function import BoundedFunction


class SimulatedAnnealing(Alg):
    def __init__(
        self,
        initial_temperature=1000,
        x1_range=(-1, 1),
        x2_range=(-1, 1),
        cooling_rate = 0.01
    ):
        super().__init__("Simulated Annealing Algorithm", x1_range, x2_range)
        self.current_temperature = initial_temperature
        self.current_solution = None
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.iteration = 0
        self.points = []

    def get_points(self) -> list[tuple[float, float]]:
        return self.points

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

    def update_points(self, f: BoundedFunction):
        self.iteration += 1
        best_f = f(self.best_pos)
        
        new_x = self.current_solution

        dx = np.random.normal(0, (self.x1_range[1] - self.x1_range[0])/10, size=1)
        dy = np.random.normal(0, (self.x2_range[1] - self.x2_range[0])/10, size=1)

        new_x = (new_x[0]+ dx[0], new_x[0]+dy[0])
        new_x = self.check_inside(new_x)

        # Calculate the change in function value
        delta_f = f(new_x) - f(self.current_solution)
        probability = np.exp(-delta_f / self.current_temperature)
        if delta_f <= 0 or np.random.rand() < probability:
            # Accept if new solution is better
            self.current_solution = new_x
            new_fitness = f(self.current_solution)
            if new_fitness < best_f:
                self.best_pos = self.current_solution
                best_f = new_fitness
        # Update temperature
        self.current_temperature = self.initial_temperature / np.log(self.iteration + 2)
        self.points.append(self.current_solution)

    def initialize_points(self):
        dimensions = 2
        self.bounds = np.array([self.x1_range, self.x2_range])
        x = np.array([np.random.uniform(b[0], b[1]) for b in self.bounds])
        self.best_pos = x
        self.current_solution = x
