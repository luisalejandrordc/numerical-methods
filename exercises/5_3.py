import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.finding_roots import FindingRoots


def f(x):
    return -25 + 82 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5


fr = FindingRoots(precision=0.002)
fr.graphical_method(f, 0.5, 1.0)
fr.bisection_method(f, 0.5, 1.0)
