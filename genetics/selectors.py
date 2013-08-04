import random
import bisect
import itertools


def tournament(tournament_size):
    def tournament_selector(population, num_parents):
        for _ in range(num_parents):
            yield max(random.sample(population, tournament_size))
    return tournament_selector


def roulette(population, num_parents):
    #Uses code taken from
    #http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice

    cumulative_scores = list(itertools.accumulate(member.score for member in population))
    total = cumulative_scores[-1]

    for _ in range(num_parents):
        rand = random.random() * total
        yield population[bisect.bisect(cumulative_scores, rand)]


def stochastic(population, num_parents):
    cumulative_scores = list(itertools.accumulate(member.score for member in population))
    total = cumulative_scores[-1]
    average = total / num_parents

    rand = random.random() * average

    for float_index, _ in zip(itertools.count(rand, average), range(num_parents)):
        yield population[bisect.bisect(cumulative_scores, float_index)]
