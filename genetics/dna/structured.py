'''
Created on Aug 4, 2013

@author: nathan
'''

from .segment import DNASegment


def structured_segment(*ordered_types):
    types_table = {cls.__name__: i for i, cls in enumerate(ordered_types)}

    class StructuredSegment(DNASegment):
        def initial_components(self):
            return (Type() for Type in ordered_types)

        def __getattr__(self, name):
            return self.components[types_table[name]]

    return StructuredSegment


def arrayed_segment(length, repeated_type):
    class ArrayedSegment(DNASegment):
        def initial_components(self):
            return (repeated_type() for _ in range(length))

    return ArrayedSegment

# TODO: add binary dna
