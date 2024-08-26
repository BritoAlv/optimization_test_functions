from alg import Example
from bat_algorithm import Bat
from front_plot import *
from bounded_function import rotated_elipse2, scahffer3, ackley, beale, schaffer2
from particle_swarm import ParticleSwarm
from sfla import SFLA

"""
call this function passing an Algoritm and a Function to Test.
"""
# front_plot(Bat(60), beale)

front_plot(SFLA(
    name='Schaffer No. 2', 
    objective_function=schaffer2.f, 
    m=100, 
    n=50,
    dimension=2,
    N=10, 
    q=10, 
    S=100
    ), schaffer2)