from dataclasses import dataclass
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Result:
    success: bool = False
    root: float = 0
    iterations: int = 0


class FindingRoots:
    def __init__(
        self,
        max_iterations: int = 10,
        precision: float = 0.001,
        print_iterations: bool = True,
    ) -> None:
        self.max_iterations = max_iterations
        self.precision = precision
        self.print_iterations = print_iterations

    def _opposite_signs(self, a: float, b: float):
        return (a < 0 < b) or (b < 0 < a)

    def graphical_method(self, f: Callable, x_l: float, x_u: float) -> None:
        x = np.linspace(x_l, x_u, 1000)
        h_line = np.zeros(1000)
        plt.figure(figsize=(10, 6))
        plt.plot(x, f(x), color="#1982c4")
        plt.plot(x, h_line, color="#ff595e")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Graphical Method for Finding Roots")
        plt.show()

    def bisection_method(self, f: Callable, a: float, b: float) -> Result:
        c = (a + b) / 2
        f_a, f_b, f_c = f(a), f(b), f(c)
        if f_a == 0:
            return Result(success=True, root=a)
        if f_b == 0:
            return Result(success=True, root=b)
        if not self._opposite_signs(f_a, f_b):
            return Result()
        iteration = 1
        while iteration <= self.max_iterations:
            c = (a + b) / 2
            f_c = f(c)
            if self.print_iterations:
                print(f"Iteration {iteration}:", end="\t")
                print(f"a = {a:.5f}", end="\t")
                print(f"b = {b:.5f}", end="\t")
                print(f"c = {c:.5f}", end="\t")
                print(f"f(c) = {f_c:.5f}")
            if abs(f_c) <= self.precision:
                return Result(True, c, iteration)
            if self._opposite_signs(f_a, f_c):
                b, f_b = c, f_c
            else:
                a, f_a = c, f_c
            iteration += 1
        return Result(True, c, iteration - 1)
