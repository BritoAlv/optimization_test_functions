from bat_algorithm import Bat
from plots import *
from bounded_function import rotated_elipse2, scahffer3, ackley, beale, schaffer2, ripple25, booth
from gradient_descent import GradientDescent
from particle_swarm import ParticleSwarm
from sfla import SFLA

"""
call this function passing an Algoritm and a Function to Test.
"""
two_plot(Bat(20, booth.range_x1, booth.range_x2), ParticleSwarm(20, booth.range_x1, booth.range_x2), booth)