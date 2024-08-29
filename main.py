from bat_algorithm import Bat
from plots import *
from bounded_function import (
    rotated_elipse2,
    scahffer3,
    ackley,
    beale,
    schaffer2,
    ripple25,
    booth,
    bukin,
)
from gradient_descent import GradientDescent
from particle_swarm import ParticleSwarm
from sfla import SFLA

"""
call this function passing an Algoritm and a Function to Test.
"""

one_plot([Bat(50), ParticleSwarm(50)], bukin)