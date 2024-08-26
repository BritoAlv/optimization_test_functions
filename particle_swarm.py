import numpy as np
from alg import Alg
from bounded_function import BoundedFunction


class ParticleSwarm(Alg):
    def __init__(self, number_particles=50):
        super().__init__("Particle Swarm")
        self.number_particles = number_particles
        self.inertia = 0.2
        self.accel_personal = 0.01
        self.accel_social = 0.05
        self.particles = [
            (
                np.random.uniform(self.x1_range[0], self.x1_range[1]),
                np.random.uniform(self.x2_range[0], self.x2_range[1]),
            )
            for _ in range(self.number_particles)
        ]
        self.fitness: None | list[float] = None
        self.particles_best_position = self.particles
        self.particle_best_fitness : None | list[float] = None
        self.best_value : None | float = None
        self.best_pos : None | tuple[float, float] = None
        self.velocity = [(float(0), float(0)) for _ in range(self.number_particles)]

    def get_points(self) -> list[tuple[float, float]]:
        return self.particles

    def update_points(self, bf: BoundedFunction):
        if self.fitness == None:
            self.fitness = [bf(x) for x in self.particles]
            self.particle_best_fitness = self.fitness.copy()
            self.best_value = min(self.fitness)
            self.best_pos = self.particles[np.argmin(self.fitness)]
            return
        assert(self.best_pos != None)
        assert(self.particle_best_fitness != None)
        assert(self.best_value != None)
        for i in range(self.number_particles):
            v1_x  = self.inertia * self.velocity[i][0]
            v1_y = self.inertia * self.velocity[i][1]

            v2_x = self.accel_personal * np.random.uniform(0, 1) * (self.particles_best_position[i][0] - self.particles[i][0])
            v2_y = self.accel_personal * np.random.uniform(0, 1) * (self.particles_best_position[i][1] - self.particles[i][1])

            v3_x = self.accel_social * np.random.uniform(0, 1) * (self.best_pos[0] - self.particles[i][0])
            v3_y = self.accel_social * np.random.uniform(0, 1) * (self.best_pos[1] - self.particles[i][1])

            self.velocity[i] = (v1_x + v2_x + v3_x, v1_y + v2_y + v3_y)
            
            self.update_particle_pos(i, self.velocity[i])

            self.fitness[i] = bf.f(self.particles[i][0], self.particles[i][1])
            if self.fitness[i] < self.particle_best_fitness[i]:
                self.particle_best_fitness[i] = self.fitness[i]
                self.particles_best_position[i] = self.particles[i]

            if self.fitness[i] < self.best_value:
                self.best_value = self.fitness[i]
                self.best_pos = self.particles[i]

        print(f"Current best is {self.best_value} at {self.best_pos}")

    
            
    def update_particle_pos(self, index : int, new_vel : tuple[float, float]):
        x = self.particles[index][0]
        y = self.particles[index][1]

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

        self.particles[index] = (x, y)