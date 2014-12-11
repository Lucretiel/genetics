import abc


class DNABase(metaclass=abc.ABCMeta):
    '''
    DNABase is the base class for all dna. It defines the abstract methods that
    all DNA should have, as well as an __lt__ method for sorting.
    '''
    #__slots__ = ('score',)

    #TODO: Add helpers for calling type(self)(...) everywhere
    @abc.abstractmethod
    def mutate(self, mask):
        '''
        This method should return a DNA object that is the result of applying
        the mutation mask to each component of this DNA. It is allowed to
        return self if and only if the mask application doesn't change the dna
        at all.
        '''
        pass

    @abc.abstractmethod
    def combine(self, other, mask):
        '''
        Return a tuple of two new DNAs that are the result of combining this
        DNA with other, using the mask.
        '''
        pass

    @classmethod
    def total_length(cls):
        '''
        This method is provided for backwards compatibility, and returns the
        total length of this DNA. For DNA with subcomponents, this is the sum
        of the lengths of the subcomponents. This is now computed beforehand
        and stored in a class-scope variable. Deprecated.
        '''
        return cls.static_length


def combine_element_pairs(pairs):
    '''
    When given an iterable that returns pairs- such as
    [(1, 2), (3, 4), (5, 6)] combine them into a pair of iterables, such as
    ((1, 3, 5), (2, 4, 6))
    '''

    return tuple(zip(*pairs))
