import abc
from .base import DNABase


class DNAComponent(DNABase, metaclass=abc.ABCMeta):
    '''
    A dna component is a single, indivisible value in the dna. It is an ABC and
    should be subclassed with a mutate_value() function. It should NOT overload
    and of the other methods, including __init__.
    '''
    def __init__(self, initial_value=None):
        if initial_value is None:
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

    @abc.abstractmethod
    def mutate_value(self):
        pass
