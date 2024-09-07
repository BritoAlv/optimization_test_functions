from plot.bat_algorithm import Bat
from plot.plots import *
from plot.bounded_function import (
    rotated_elipse2,
    scahffer3,
    ackley,
    beale,
    schaffer1,
    schaffer2,
    ripple25,
    booth,
    bukin,
)
from plot.gradient_descent import GradientDescent
from plot.particle_swarm import ParticleSwarm
from plot.sfla import SFLA
from plot.simulated_annealing import SimulatedAnnealing
from plot.genetic_alg_interfaz import Genetic_Algorithm

"""
call this function passing an Algoritm and a Function to Test.
"""

one_plot([
    SimulatedAnnealing(),
    Genetic_Algorithm(), 
    ParticleSwarm(10), 
    Bat(20),
    SFLA("Shuffled Frog Leaping Algorithm",bukin.f, 10, 10, 2, 6,6, 100, bounds=(-100, 100))], bukin)