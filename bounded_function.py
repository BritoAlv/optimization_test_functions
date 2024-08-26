from typing import Callable
import numpy as np

class BoundedFunction:
    def __init__(self, name : str, f : Callable[[float, float], float] , range_x1 : tuple[float, float], range_x2 : tuple[float, float], glob_min : tuple[tuple[float, float], float]) -> None:
        self.name = name
        self.f = f
        self.range_x1 = range_x1
        self.range_x2 = range_x2
        self.glob_min = glob_min

    def __call__(self, point : tuple[float, float]) -> float:
        return self.f(point[0], point[1])
    
def _ch(x1, x2):
    num = (np.sin(np.cos(np.abs(x1**2 - x2**2))))**2 - 0.5
    den = 1 + 0.001*(x1**2 + x2**2)**2
    return 0.5 + num/den

scahffer3 = BoundedFunction("Scahffer3", _ch, (-2, 2), (-2, 2), ( ( 0, 1.253115), 0.00156685))

rotated_elipse2 = BoundedFunction("Rotated Elipse 2", lambda x, y : x**2 - x*y + y**2, (-500, 500), (-500, 500), ((0, 0),0))

def _ackley(x1, x2):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x1**2 + x2**2))) - np.exp(0.5*(np.cos(2*np.pi*x1) + np.cos(2*np.pi*x2))) + np.e + 20

ackley = BoundedFunction("Ackley", _ackley, (-5, 5), (-5, 5), ((0, 0),0)) 

def _beale(x1, x2):
    return (1.5 - x1 + x1*x2)**2 + (2.25 - x1 + x1*x2**2)**2 + (2.625 - x1 + x1*x2**3)**2

beale = BoundedFunction("Beale", _beale, (-4.5, 4.5), (-4.5, 4.5), ((3, 0.5), 0))

def schaffer_no_2(x1, x2):
    return 0.5 + ((np.sin((x1**2 - x2**2)**2))**2 - 0.5) / (1 + 0.001 * ((x1**2 + x2**2)**2))

schaffer2 = BoundedFunction("Schaffer No. 2", schaffer_no_2, (-100, 100), (-10, 10), ((0, 0), 0))