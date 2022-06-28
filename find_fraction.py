from numpy import around


def find_fraction(fraction: float) -> int:
    for i in range(1, 50):
        for j in range(1, 50):
            if around(i/j, 2) == fraction:
                return j
    return 1
