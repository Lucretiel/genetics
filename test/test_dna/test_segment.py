from genetics.dna.segment import DNASegment
from genetics.dna.component import DNAComponent


class MutatingComponent(DNAComponent):
    def initial_value(self):
        return 0

    def mutate_value(self):
        return 1


class MutatingSegment(DNASegment):
    def initial_components(self):
        return [MutatingComponent() for _ in range(20)]


class NestedMutatingSegment(DNASegment):
    def initial_components(self):
        return [MutatingSegment() for _ in range(5)]


def test_total_length():
    x = MutatingSegment()
    assert x.total_length() == 20


def test_nested_total_length():
    x = NestedMutatingSegment()
    assert x.total_length() == 100


def test_length():
    x = MutatingSegment()
    assert len(x) == 20


def test_nested_length():
    x = NestedMutatingSegment()
    assert len(x) == 5


def test_iteration():
    x = MutatingSegment()

    for a, b in zip(x, x.components):
        assert a is b


def test_item_access():
    x = MutatingSegment()

    for i in range(20):
        assert x[i] is x.components[i]
