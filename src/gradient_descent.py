import numpy as np
from alg import Alg
from bounded_function import BoundedFunction


class GradientDescent(Alg):
    def __init__(self, number_points = 40, x1_range = (-1, 1), x2_range = (-1, 1)):
        super().__init__("Gradient Descent", x1_range, x2_range)
        self.number_points = number_points
        self.step_size = 0.01
        self.points = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(self.number_points)
        ]

    def get_points(self) -> list[tuple[float, float]]:
        return self.points
    
    def update_points(self, bf: BoundedFunction):
        if self.best_pos == None:
            fitness = [bf(x) for x in self.points]
            self.best_pos = self.points[np.argmin(fitness)]
            return
        if bf.gradient == None:
            raise ValueError("Gradient method but function doesn't provide gradient")
        for i in range(self.number_points):
            pos_x = self.points[i][0]
            pos_y = self.points[i][1]
            self.update_pos(i, (-self.step_size * bf.gradient[0](pos_x, pos_y), -self.step_size * bf.gradient[1](pos_x, pos_y)))

    def update_pos(self, index : int, new_vel : tuple[float, float]):
        x = self.points[index][0]
        y = self.points[index][1]

        x += new_vel[0]
        y += new_vel[1]

        if x < self.x1_range[0]:
            x = self.x1_range[0]
        if x > self.x1_range[1]:
            x = self.x1_range[1]

        if y < self.x2_range[0]:
            y = self.x2_range[0]
        if y > self.x2_range[1]:
            y = self.x2_range[1]

        self.points[index] = (x, y)     