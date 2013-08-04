from genetics import mutation
import itertools


def test_no_mutation():
    for m in itertools.islice(mutation.mutation_rate(0)(100), 100):
        assert m is False


def test_all_mutation():
    for m in itertools.islice(mutation.mutation_rate(1)(100), 100):
        assert m is True


def test_some_mutation():
    for rate in (.25, .5, .75):
        values = set()
        for m in itertools.islice(mutation.mutation_rate(rate)(100), 100):
            values.add(m)
        assert True in values and False in values