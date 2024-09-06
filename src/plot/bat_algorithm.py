import numpy as np
from plot.alg import Alg
from plot.bounded_function import BoundedFunction

class Bat(Alg):
    def __init__(self, number_bats = 40, x1_range = (-1, 1), x2_range = (-1, 1)):
        super().__init__("Bat Algorithm", x1_range, x2_range)
        self.number_bats = number_bats
        self.freq_min = 0
        self.freq_max = 5
        self.Loudness = 0.5
        self.Pulse_rate = 0.5
        self.gamma = 0.5
        self.iterations = 0
        self.bats = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(self.number_bats)
        ]
        self.loudness = [float(1) for _ in range(self.number_bats)]
        self.pulse_rate = [float(0) for _ in range(self.number_bats)]
        self.frequency = [float(0) for _ in range(self.number_bats)]
        self.velocity = [(float(0), float(0)) for _ in range(self.number_bats)]

        self.fitness: None | list[float] = None
        self.best_value : None | float = None

    def get_points(self) -> list[tuple[float, float]]:
        return self.bats
    
    def update_points(self, bf: BoundedFunction):
        if self.fitness == None:
            self.fitness = [bf(x) for x in self.bats]
            self.best_value = min(self.fitness)
            self.best_pos = self.bats[np.argmin(self.fitness)]
            return
        self.iterations += 1
        assert(self.best_pos != None)
        assert(self.best_value != None)
        for i in range(self.number_bats):
            self.frequency[i] = np.random.uniform(self.freq_min, self.freq_max)
            v1_x = (self.best_pos[0] - self.bats[i][0]) * self.frequency[i]
            v1_y = (self.best_pos[1] - self.bats[i][1]) * self.frequency[i]
            self.velocity[i] = (v1_x, v1_y) 

            tup = self.velocity[i]
            if np.random.uniform(0, 1) < self.pulse_rate[i]:
                tup = (tup[0] + np.mean(self.loudness)*np.random.uniform(0, 1), tup[1] + np.mean(self.loudness)*np.random.uniform(0, 1))

            new_pos = self.update_bat_pos(i, tup)
            new_f = bf(new_pos)
            if self.fitness[i] > new_f:
                self.fitness[i] = new_f
                self.bats[i] = new_pos
                self.loudness[i] *= self.Loudness
                self.pulse_rate[i] = self.Pulse_rate * ( 1 - np.exp(-self.gamma * self.iterations))

                if self.fitness[i] < self.best_value:
                    self.best_value = self.fitness[i]
                    self.best_pos = new_pos

    def update_bat_pos(self, index : int, new_vel : tuple[float, float]) -> tuple[float, float]:
        x = self.bats[index][0]
        y = self.bats[index][1]

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

        return (x, y)

    def initialize_points(self):
        self.bats = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(self.number_bats)
        ]