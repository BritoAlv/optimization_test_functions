from alg import Example
from bat_algorithm import Bat
from front_plot import *
from bounded_function import rotated_elipse2, scahffer3, ackley, beale
from particle_swarm import ParticleSwarm

"""
call this function passing an Algoritm and a Function to Test.
"""
front_plot(Bat(60), beale)