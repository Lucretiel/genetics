import random
from .base import DNABase, combine_element_pairs

class DNABaseBinary(DNABase):
    '''
    DNABinary is a relatively efficient implementation of DNA in which each
    component is only a bit. Use a subclass with static_length, or the function
    fixed_dna_binary, to create a fixed-length Binary DNA.
    '''
    __slots__ = ('bits', )

    @staticmethod
    def bit():
        return random.choice((False, True))

    def __init__(self, bits=None):
        if bits is None:
            self.bits = [bit() for _ in range(self.static_length)]

        #Allows for initializers of the form '1000101'
        elif isinstance(bits, str):
            self.bits = [bool(int(bit)) for bit in bits]

        else:
            self.bits = bits

    def mutate(self, mutate_mask):
        return type(self)(tuple(self.bit() if mask else bit for bit, mask in
            zip(self.bits, mutate_mask)))

    def combine(self, other, combine_mask):
        child1, child2 = combine_element_pairs((c1, c2) if mask else (c2, c1)
            for c1, c2, mask in zip(self, other, combine_mask))

        return DNABinary(child1), DNABinary(child2)

    @property
    def components(self):
        '''
        Retained for backwards compatibility: Originally the data in a Binary
        DNA was called components. To distinguish it from Segments, it was
        renamed bits. Deprecated and will be removed in a future release.
        '''
        return self.bits

    #iteration
    def __iter__(self):
        return iter(self.bits)

    def __len__(self):
        return len(self.bits)

    def __getitem__(self, index):
        return self.bits[index]

class DNABinary(DNABaseBinary):
    '''
    Retained for backwards compatibility: The old, dynamically sized DNABinary.
    '''
    def __init__(self, bits):
        #Allows for int initializers to create a DNABinary of that length
        if isinstance(bits, int):
            bits = [self.bit() for _ in range(bits)]
        DNABaseBinary.__init__(self, bits)

    def total_length(self):
        return len(self.bits)
