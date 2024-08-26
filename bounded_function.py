from typing import Callable
import numpy as np

class BoundedFunction:
    def __init__(self, name : str, f : Callable[[float, float], float] , range_x1 : tuple[float, float], range_x2 : tuple[float, float]) -> None:
        self.name = name
        self.f = f
        self.range_x1 = range_x1
        self.range_x2 = range_x2

    def __call__(self, point : tuple[float, float]) -> float:
        return self.f(point[0], point[1])
    
def _ch(x1, x2):
    num = (np.sin(np.cos(np.abs(x1**2 - x2**2))))**2 - 0.5
    den = 1 + 0.001*(x1**2 + x2**2)**2
    return 0.5 + num/den

chapter3 = BoundedFunction("Chapter3", _ch, (-2, 2), (-2, 2))

rotated_elipse2 = BoundedFunction("Rotated Elipse 2", lambda x, y : x**2 - x*y + y**2, (-500, 500), (-500, 500))

def _ackley(x1, x2):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x1**2 + x2**2))) - np.exp(0.5*(np.cos(2*np.pi*x1) + np.cos(2*np.pi*x2))) + np.e + 20

ackley = BoundedFunction("Ackley", _ackley, (-5, 5), (-5, 5))