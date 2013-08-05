from .base import DNABase


class DNAComponent(DNABase):
    '''
    A dna component is a single, indivisible value in the dna. Subclasses
    should provide a mutate_value() for mutation and an initial_value()
    function for argument-free initialization. If no initial_value function
    exists, mutate_value will be used
    '''
    def __init__(self, initial_value=None):
        if initial_value is None:
            try:
                self.value = self.initial_value()
            except AttributeError:
                self.value = self.mutate_value()
        else:
            self.value = initial_value

    def total_length(self):
        return 1

    def mutate(self, mutate_mask):
        if next(iter(mutate_mask)):
            return type(self)(self.mutate_value())
        else:
            return self

    def combine(self, other, cross_mask):
        if next(iter(cross_mask)):
            return (self, other)
        else:
            return (other, self)
