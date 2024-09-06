import numpy as np
from plot.alg import Alg
from plot.bounded_function import BoundedFunction

class SimulatedAnnealing(Alg):
    def __init__(self, initial_temperature=1000, cooling_rate=0.99, final_temperature= 0.01, max_iterations=100000, x1_range = (-1, 1), x2_range = (-1, 1)):
        super().__init__("Simulated Annealing Algorithm", x1_range, x2_range)
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.final_temperature = final_temperature
        self.temperature = initial_temperature
        self.max_iterations = max_iterations
        self.current_temperature = initial_temperature
        self.best_solution = None
        self.function_value = None
        self.current_solution = None
        self.bounds = None
        self.point = []

    def get_points(self) -> list[tuple[float, float]]:
        return self.point

    def update_points(self, f : BoundedFunction):
        best_f = f(self.current_solution)
        self.best_pos = self.best_solution.copy()
        new_x = self.x + np.random.normal(0, 0.1, size=len(self.bounds))
        new_x = np.clip(new_x, self.bounds[:, 0], self.bounds[:, 1])
        
        # Calculate the change in function value
        delta_f = f(new_x) - f(self.x)
        
        if delta_f <= 0:
            # Accept if new solution is better
            self.x = new_x
            if f(self.x) < best_f:
                self.best_solution = self.x.copy()
                best_f = f(self.x)
                self.point.append(self.x)
        else:
            # Accept with probability based on temperature
            probability = np.exp(-delta_f / self.temperature)
            if np.random.rand() < probability:
                self.x = new_x
                if f(self.x) < best_f:
                    self.best_solution = self.x.copy()
                    best_f = f(self.x)
                    self.point.append(self.x)
        
        # Update temperature
        self.temperature *= self.cooling_rate  # Cooling schedule
        if self.temperature <= self.final_temperature:
            return
 
    def initialize_points(self):
        dimensions = 2
        self.bounds = np.array([(-100, 100), (-100, 100)])
        x = np.array([np.random.uniform(b[0], b[1]) for b in self.bounds])
        self.initial_point = x.copy()
        self.best_solution = x.copy() 
        self.x = x.copy()
        self.current_solution = x.copy()

 