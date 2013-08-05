genetics
========

A python library for genetic algorithms

Example
=======

Finding Hello World
-------------------

	import string
	import random
	
	import genetics
	
	letters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
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
	
	    if best_score >= 10:
	        break
	
	    population = sim.step(population)
		
**Sample Output**:

	HhGAv,>s$./` | Average score: 0.14
	ccyPoVuV(j"! | Average score: 0.31
	ccyPoVuV(j"! | Average score: 0.59
	ccyPoVuV(j"! | Average score: 0.87
	=e~LoVuV(j"! | Average score: 1.17
	=e~LoVuV(j"! | Average score: 1.53
	jeyPoV-o?t"! | Average score: 1.96
	HeyPoV-o?t"! | Average score: 2.37
	HeyPoV-o?t"! | Average score: 2.82
	HeyPoV-o?t"! | Average score: 3.19
	HeyPoV-o?t"! | Average score: 3.55
	HeyPoV-o?t"! | Average score: 3.91
	HePvoVuozTd! | Average score: 4.2
	HePvoVuozTd! | Average score: 4.54
	HePvoVuozTd! | Average score: 5.01
	He(/oVNoUld! | Average score: 5.39
	He(/oVNoUld! | Average score: 5.69
	HeyloV-oeld! | Average score: 5.97
	HeyloV-oeld! | Average score: 6.24
	HeyloV-oeld! | Average score: 6.55
	HeyloV-oeld! | Average score: 7.07
	HeyloV-oeld! | Average score: 7.23
	HeyloV-oeld! | Average score: 7.39
	HeyloV-oeld! | Average score: 7.62
	HeyloV-oeld! | Average score: 7.87
	HeyloV-oeld! | Average score: 7.9
	HeyloV-oeld! | Average score: 7.93
	HeyloV-oeld! | Average score: 7.91
	HeyloV-oeld! | Average score: 7.91
	HeyloV-oeld! | Average score: 7.91
	HeyloV-oeld! | Average score: 7.88
	HeyloV-oeld! | Average score: 7.87
	HeyloV-oeld! | Average score: 7.87
	HeyloV-oeld! | Average score: 7.9
	HeyloV-oeld! | Average score: 7.89
	HeyloV-oeld! | Average score: 7.88
	HeyloV-oeld! | Average score: 7.88
	HeyloV-oeld! | Average score: 7.91
	HeyloV-oeld! | Average score: 7.88
	HeyloV-oeld! | Average score: 7.96
	HeyloV-oeld! | Average score: 7.89
	HeyloV-oeld! | Average score: 7.91
	HeyloV-oeld! | Average score: 7.94
	HeyloV-oeld! | Average score: 7.9
	HeyloV-oeld! | Average score: 7.94
	HeyloV-oeld! | Average score: 7.9
	HeyloVWoeld! | Average score: 7.92
	HeyloVWoeld! | Average score: 7.91
	HeyloVWoeld! | Average score: 8.09
	HeyloVWoeld! | Average score: 8.23
	HeyloVWoeld! | Average score: 8.34
	HeyloVWoeld! | Average score: 8.64
	HeyloVWoeld! | Average score: 8.82
	HeyloVWorld! | Average score: 8.83
