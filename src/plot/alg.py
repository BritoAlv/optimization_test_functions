from abc import ABC, abstractmethod

from plot.bounded_function import BoundedFunction

class Alg(ABC):
    def __init__(self, name: str, x1_range = (-1, 1), x2_range = (-1, 1)):
        self.name = name
        self.x1_range = x1_range
        self.x2_range = x2_range
        self.best_pos = None

    @abstractmethod
    def get_points(self) -> list[tuple[float, float]]:
        """
        return all the points / animals in the grid.
        """
        pass

    @abstractmethod
    def update_points(self, bf : BoundedFunction):
        """
        perform one iteration step
        """
        pass

    def log_state(self, bf : BoundedFunction):
        print(f"From {self.name}: Current best is {round(bf.f(self.best_pos[0], self.best_pos[1]), 4)} at {self.best_pos} while real is {bf.glob_min[1]} at ({bf.glob_min[0][0]}, {bf.glob_min[0][1]})")

    @abstractmethod
    def initialize_points(self):
        pass