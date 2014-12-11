import itertools
import random


def one_point_crossover(length):
    point = random.randint(0, length)
    yield from itertools.repeat(True, point)
    yield from itertools.repeat(False, length - point)


def two_point_crossover(length):
    point1, point2 = sorted(random.randint(0, length) for _ in range(2))
    yield from itertools.repeat(True, point1)
    yield from itertools.repeat(False, point2 - point1)
    yield from itertools.repeat(True, length - point2)


def uniform_point_crossover(length):
    return (random.choice((False, True)) for i in range(length))
