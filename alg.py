from abc import ABC, abstractmethod
import numpy as np

from bounded_function import BoundedFunction

class Alg(ABC):
    def __init__(self, name: str):
        self.name = name
        self.x1_range = (-1, 1)
        self.x2_range = (-1, 1)
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
        print(f"Current best is {bf.f(self.best_pos[0], self.best_pos[1])} at {self.best_pos} while real is {bf.glob_min[1]} at ({bf.glob_min[0][0]}, {bf.glob_min[0][1]})")

    def set_range(self, x1_range: tuple[float, float], x2_range: tuple[float, float]):
        """
        set the range of values to initialize and use the algorithm
        """
        self.x1_range = x1_range
        self.x2_range = x2_range


class Example(Alg):
    def __init__(self):
        super().__init__("Example for Doc")
        self.points = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(100)
        ]
        pass

    def get_points(self) -> list[tuple[float, float]]:
        return self.points

    def update_points(self, bf : BoundedFunction):
        self.points = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(100)
        ]
