genetics
========

A python library for genetic algorithms

Example
=======

Finding Hello World
-------------------

```python
import string
import random

import genetics

letters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + ' '
solution = 'Hello World!'

class LetterComponent(genetics.DNAComponent):
    def mutate_value(self):
        return random.choice(letters)

class WordDNA(genetics.arrayed_segment(len(solution), LetterComponent)):
    @property
    def score(self):
        return sum(1 if comp.value == letter else 0 for comp, letter in
                   zip(self, solution))

    def __str__(self):
        return ''.join(comp.value for comp in self)

sim = genetics.DiscreteSimulation(
    population_size=100,
    mutation_mask=genetics.mutation_rate(0.01),
    crossover_mask=genetics.one_point_crossover,
    selection_function=genetics.tournament(2),
    elite_size=2,
    initial_generator=WordDNA)


def dna_stats(population):
    '''Best DNA, best score, average score'''
    best_dna = max(population)
    best_score = best_dna.score
    average_score = sum(member.score for member in population) / len(population)

    return best_dna, best_score, average_score


population = sim.initial_population()

while True:
    best, best_score, average_score = dna_stats(population)

    print('{} | Average score: {}'.format(str(best), average_score))

    if str(best) == solution:
        break

    population = sim.step(population)
```
		
**Sample Output**:

```
&~$lo,{j'"wi | Average score: 0.148
&~$lo,{j'"wi | Average score: 0.292
H)Xl] ?lDf{@ | Average score: 0.506
H)Xlo {lZ!&@ | Average score: 0.816
H)Xlo {lZ!&@ | Average score: 1.154
HSlldpWjr`z> | Average score: 1.574
HeXyoKWqrl&K | Average score: 2.136
uello*c,rl"! | Average score: 2.722
uello*c,rl"! | Average score: 3.338
Heslo LKrlk! | Average score: 3.814
Heslo LKrlk! | Average score: 4.492
H(llooWIrld! | Average score: 5.258
Hello W,rl]! | Average score: 5.934
HeDlo World! | Average score: 6.628
HeDlo World! | Average score: 7.362
Hello World! | Average score: 8.004
```
