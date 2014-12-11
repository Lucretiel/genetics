import random


def mutation_rate(rate):
    def mutation_mask(length):
        return (random.random() < rate for _ in range(length))
    return mutation_mask
