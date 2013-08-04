import random


def mutation_rate(rate):
    def mutation_mask(length):
        return (True if random.random() < rate else False for _ in range(length))
    return mutation_mask
