import random
from genetics.dna.binary import DNABinary


def test_basic_init():
    init = (True, False, True, True, False, False, False, True, True, False)
    x = DNABinary(init)

    for component, b in zip(x, init):
        assert component == b


def test_string_init():
    init = '1000101011110101010010100101001010101110101010000000111'
    x = DNABinary(init)

    def convert_ones_zeroes(c):
        if c == '1':
            return True
        elif c == '0':
            return False
        return None

    init_bools = [convert_ones_zeroes(c) for c in init]

    for component, b in zip(x, init_bools):
        assert component == b


def test_length_init():
    x = DNABinary(100)

    assert len(x) == 100

    for component in x:
        assert component is True or component is False


def test_total_length():
    x = DNABinary(100)
    assert x.total_length() == 100


def test_deterministic_combine():
    dna1 = DNABinary(True for _ in range(100))
    dna2 = DNABinary(False for _ in range(100))

    combine_mask = [True if i < 25 else False for i in range(100)]

    dna3, dna4 = dna1.combine(dna2, combine_mask)

    for component1, component2, mask in zip(dna3, dna4, combine_mask):
        if mask:
            assert component1 is True
            assert component2 is False
        else:
            assert component1 is False
            assert component2 is True


def test_random_combine():
    dna1 = DNABinary(100)
    dna2 = DNABinary(100)

    combine_mask = [random.choice((True, False)) for _ in range(100)]

    dna3, dna4 = dna1.combine(dna2, combine_mask)

    for parent1, parent2, child1, child2, mask in zip(dna1, dna2, dna3, dna4, combine_mask):
        if mask:
            assert child1 == parent1
            assert child2 == parent2
        else:
            assert child1 == parent2
            assert child2 == parent1


def test_mutation():
    dna = DNABinary(False for _ in range(100))

    mask = [True if i % 2 == 0 else False for i in range(100)]

    mutated = dna.mutate(mask)

    # Test that the original DNA is untouched
    for b in dna:
        assert b is False

    for b, mask in zip(mutated, mask):
        if not mask:
            assert b is False


def test_element_access():
    x = [True, False, False, True]

    dna = DNABinary(x)

    for i in range(4):
        assert dna[i] == x[i]
