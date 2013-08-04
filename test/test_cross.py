from genetics import cross
import itertools


def mask_run(mask, b):
    for m in mask:
        if m is (not b):
            break
        assert m is b


def test_one_point_crossover():
    mask = itertools.islice(cross.one_point_crossover(100), 100)

    mask_run(mask, True)

    for m in mask:
        assert m is False


def test_two_point_crossover():
    mask = itertools.islice(cross.two_point_crossover(100), 100)

    mask_run(mask, True)
    mask_run(mask, False)

    for m in mask:
        assert m is True


def test_uniform_point_crossover():
    mask = itertools.islice(cross.uniform_point_crossover(100), 100)

    values = set()
    for m in mask:
        values.add(m)
    assert True in values and False in values