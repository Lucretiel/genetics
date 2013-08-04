import random
from .base import DNABase, combine_element_pairs


class DNABinary(DNABase):
    '''
    DNABinary is a relatively efficient implementation of DNA in which each
    component is only a bit.
    '''
    def __init__(self, bits):
        #Allows for initializers of the form '1000101'
        if isinstance(bits, str):
            bits = map(int, bits)

        #Allows for length initializers
        if isinstance(bits, int):
            bits = (random.choice((True, False)) for _ in range(bits))
        self.components = tuple(map(bool, bits))

    def total_length(self):
        return len(self.components)

    def mutate(self, mutate_mask):
        return DNABinary(random.choice((True, False)) if mask else c
                         for c, mask in zip(self.components, mutate_mask))

    def combine(self, other, combine_mask):
        def combine_generator():
            for c1, c2, mask in zip(self, other, combine_mask):
                yield (c1, c2) if mask else (c2, c1)

        child1, child2 = combine_element_pairs(combine_generator())

        return DNABinary(child1), DNABinary(child2)

    #iteration
    def __iter__(self):
        return iter(self.components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]
