from alg import Example
from front_plot import *
from bounded_function import rotated_elipse2, chapter3, ackley
from particle_swarm import ParticleSwarm

"""
call this function passing an Algoritm and a Function to Test.
"""
front_plot(ParticleSwarm(), ackley)