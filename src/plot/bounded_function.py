import math
from typing import Callable
import numpy as np


class BoundedFunction:
    def __init__(
        self,
        name: str,
        f: Callable[[float, float], float],
        range_x1: tuple[float, float],
        range_x2: tuple[float, float],
        glob_min: tuple[tuple[float, float], float],
        gradient: (
            None
            | tuple[Callable[[float, float], float], Callable[[float, float], float]]
        ) = None,
    ) -> None:
        self.name = name
        self.f = f
        self.range_x1 = range_x1
        self.range_x2 = range_x2
        self.glob_min = glob_min
        self.gradient = gradient
        self.calls = 0

    def __call__(self, point: tuple[float, float]) -> float:
        self.calls += 1
        return self.f(point[0], point[1])


def _ch(x1, x2):
    num = (np.sin(np.cos(np.abs(x1**2 - x2**2)))) ** 2 - 0.5
    den = 1 + 0.001 * (x1**2 + x2**2) ** 2
    return 0.5 + num / den


scahffer3 = BoundedFunction(
    "Scahffer3", _ch, (-2, 2), (-2, 2), ((0, 1.253115), 0.00156685)
)

def _rosenbrock(x1, x2, a = 1, b = 10):
    return (a-x1)**2 + b*(x2 - x1**2)**2

def _rosenbreck_gradient_x(x1, x2, a= 1, b = 10):
    return 2*(x1-a) - 4*b*x1*(x2-x1**2)

def _rosenbreck_gradient_y(x1, x2, a= 1, b = 10):
    return 2*b*(x2-x1**2)


rosenbrock = BoundedFunction("Rosenbrock", _rosenbrock, (-2, 2), (-2, 2), ((1, 1), 0), gradient=(_rosenbreck_gradient_x, _rosenbreck_gradient_y))

rotated_elipse2 = BoundedFunction(
    "Rotated Elipse 2",
    lambda x, y: x**2 - x * y + y**2,
    (-500, 500),
    (-500, 500),
    ((0, 0), 0),
)


def _ackley(x1, x2):
    return (
        -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2)))
        - np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2)))
        + np.e
        + 20
    )


ackley = BoundedFunction("Ackley", _ackley, (-5, 5), (-5, 5), ((0, 0), 0))


def _beale(x1, x2):
    return (
        (1.5 - x1 + x1 * x2) ** 2
        + (2.25 - x1 + x1 * x2**2) ** 2
        + (2.625 - x1 + x1 * x2**3) ** 2
    )


beale = BoundedFunction("Beale", _beale, (-4.5, 4.5), (-4.5, 4.5), ((3, 0.5), 0))

def schaffer_no_1(x1, x2):
    return 0.5 + ((np.sin((x1**2 + x2**2)**2))**2 - 0.5) / (1 + 0.001 * ((x1**2 + x2**2)**2))

schaffer1 = BoundedFunction("Schaffer No. 1", schaffer_no_1, (-100, 100), (-100, 100), ((0, 0), 0), gradient=())

def schaffer_no_2(x1, x2):
    return 0.5 + ((np.sin((x1**2 - x2**2) ** 2)) ** 2 - 0.5) / (
        1 + 0.001 * ((x1**2 + x2**2) ** 2)
    )


schaffer2 = BoundedFunction(
    "Schaffer No. 2", schaffer_no_2, (-100, 100), (-100, 100), ((0, 0), 0)
)


def _ripple25(x1, x2):
    ans = 0
    for x in [x1, x2]:
        ans += (
            -np.exp(-2 * np.log(2) * ((x - 0.1) / 0.8) ** 2)
            * (np.sin(5 * np.pi * x)) ** 6
        )
    return ans


ripple25 = BoundedFunction("Ripple 25", _ripple25, (0, 1), (0, 1), ((0.1, 0.1), -2))


def _booth(x1, x2):
    return (x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2


def gradient_booth_x(x1, x2):
    return 10 * x1 + 8 * x2 - 34


def gradient_booth_y(x1, x2):
    return 8 * x1 + 10 * x2 - 38


booth = BoundedFunction(
    "Booth",
    _booth,
    (-10, 10),
    (-10, 10),
    ((1, 3), 0),
    (gradient_booth_x, gradient_booth_y),
)


def _bukin(x1, x2):
    return 100 * np.sqrt(abs(x2 - 0.01 * x1**2)) + 0.01 * abs(x1 + 10)

def _mishra_7(x1, x2):
    N = 5
    return ( x1*x2 - math.factorial(N))**2

mishra_7 = BoundedFunction("Mishra 7", _mishra_7, (-10, 10), (-10, 10), ((0, 1), 0))

bukin = BoundedFunction("Bukin", _bukin, (-15, -5), (-3, 3), ((-10, 1), 0))