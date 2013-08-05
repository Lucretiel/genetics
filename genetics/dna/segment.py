from .base import DNABase, combine_element_pairs


class DNASegment(DNABase):
    def __init__(self, components=None):
        '''
        If no initializer is given, there should be an initial_components()
        '''
        if components is None:
            components = self.initial_components()
        self.components = tuple(components)

    def total_length(self):
        return sum(c.total_length() for c in self.components)

    def mutate(self, mutate_mask):
        iter_mutate_mask = iter(mutate_mask)
        return type(self)(c.mutate(iter_mutate_mask) for c in self.components)

    def combine(self, other, cross_mask):
        iter_cross_mask = iter(cross_mask)

        def combine_generator():
            for c1, c2 in zip(self, other):
                yield c1.combine(c2, iter_cross_mask)

        child1, child2 = combine_element_pairs(combine_generator())

        return type(self)(child1), type(self)(child2)

    # Iteration protocol
    def __iter__(self):
        return iter(self.components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]
