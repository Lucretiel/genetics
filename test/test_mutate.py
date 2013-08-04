from genetics import mutation
import itertools


def test_no_mutation():
    mask = list(mutation.mutation_rate(0)(100))
    assert len(mask) == 100
    for m in mask:
        assert m is False


def test_all_mutation():
    mask = list(mutation.mutation_rate(1)(100))
    assert len(mask) == 100
    for m in mask:
        assert m is True


def test_some_mutation():
    for rate in (.25, .5, .75):
        mask = list(mutation.mutation_rate(rate)(100))
        assert len(mask) == 100
        values = set()
        for m in mask:
            values.add(m)
        assert True in values and False in values
