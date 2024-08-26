from abc import ABC, abstractmethod
import numpy as np

class Alg(ABC):
    def __init__(self):
        self.x1_range = (-1, 1)
        self.x2_range = (-1, 1)

    @abstractmethod
    def get_points() -> list[tuple[float, float]]:
        pass

    @abstractmethod
    def update_points():
        pass

    def set_range(self, x1_range : tuple[float, float], x2_range : tuple[float, float]):
        self.x1_range = x1_range
        self.x2_range = x2_range


class Example(Alg):
    def __init__(self):
        super().__init__()
        self.points = [ (np.random.uniform(self.x1_range[0], self.x1_range[1]), np.random.uniform(self.x2_range[0], self.x2_range[1])) for _ in range(100) ]
        pass

    def get_points(self) -> list[tuple[float, float]]:
        return self.points
    
    def update_points(self):
        self.points = [ (np.random.uniform(self.x1_range[0], self.x1_range[1]), np.random.uniform(self.x2_range[0], self.x2_range[1])) for _ in range(100) ]