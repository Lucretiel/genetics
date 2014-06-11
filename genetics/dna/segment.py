from .base import DNABase, combine_element_pairs

class DNABaseSegment(DNABase):
    '''
    Helper class for creating DNA segments. A DNA segment is a a DNA that is
    made up of subcomponents. These subcomponents can be DNAComponents, other
    segment, or any other kind of DNA. Subclasses should implement the
    initial_components() method, which returns a tuple or of the initial
    components. Subclasses should also add a static_length class member, which
    is the total length of all the subcomponents.
    '''
    __slots__ = ('components',)

    def __init__(self, components=None):
        self.components = components or self.initial_components()

    def mutate(self, mutate_mask):
        return type(self)(tuple(c.mutate(mutate_mask)
            for c in self.components))

    def combine(self, other, cross_mask):
        child1, child2 = combine_element_pairs(
            c1.combine(c2, cross_mask) for c1, c2 in zip(self, other))

        return type(self)(child1), type(self)(child2)

    # Iteration protocol
    def __iter__(self):
        return iter(self.components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

class DNASegment(DNABaseSegment):
    '''
    This class is provided for backwards compatibility and considered
    deprecated. It computes the length each time total_length is called. In the
    current version of the library, structured techniques are used to calculate
    this value when the class is created, making this unneccesary.
    '''
    __slots__ = ()
    def total_length(self):
        return sum(c.total_length() for c in self.components)


