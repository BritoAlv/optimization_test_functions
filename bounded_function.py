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

chapter = BoundedFunction("Chapter", _ch, (-10, 10), (-10, 10))