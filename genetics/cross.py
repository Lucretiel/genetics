import itertools
import random


def one_point_crossover(length):
    point = random.randint(0, length)
    yield from itertools.repeat(True, point)
    yield from itertools.repeat(False)


def two_point_crossover(length):
    points = sorted(random.randint(0, length) for _ in range(2))
    yield from itertools.repeat(True, points[0])
    yield from itertools.repeat(False, points[1] - points[0])
    yield from itertools.repeat(True)


def uniform_point_crossover(length):
    return (random.choice((False, True)) for i in range(length))
