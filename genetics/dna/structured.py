'''
Created on Aug 4, 2013

@author: nathan
'''

from .segment import DNABaseSegment
from .binary import DNABaseBinary

def structured_segment(*ordered_types):
    '''
    Create a DNA type with the given types as components. The components can
    be accessed directly by index or attribute; the attribute name is the class
    name.
    '''
    types_table = {Type.__name__: i for i, Type in enumerate(ordered_types)}
    total_length = sum(Type.static_size for Type in ordered_types)

    class StructuredSegment(DNABaseSegment):
        static_length = total_length
        __slots__ = ()

        @staticmethod
        def initial_components():
            return tuple(Type() for Type in ordered_types)

        def __getattr__(self, name):
            return self.components[types_table[name]]

    return StructuredSegment


def arrayed_segment(length, repeated_type):
    '''
    Create a DNA type consisting of a fixed number of the same type of component
    '''
    class ArrayedSegment(DNABaseSegment):
        static_length = length * repeated_type.static_length
        __slots__ = ()

        @staticmethod
        def initial_components():
            return tuple(repeated_type() for _ in range(length))

    return ArrayedSegment

def fixed_length_binary(length):
    '''
    Create a DNABinary class of fixed length.
    '''
    class FixedDNABinary(DNABaseBinary):
        __slots__ = ()
        static_length = length

    return FixedDNABinary
