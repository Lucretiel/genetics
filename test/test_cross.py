from genetics import cross
import itertools


def mask_run(mask, b):
    '''
    Assert that there is a run of at least 0 elements that are b in the mask
    iterator.. After completion, the mask has been consumed out to the end of
    the run.
    '''
    for m in mask:
        if m is (not b):
            break
        assert m is b


def test_one_point_crossover():
    mask = list(cross.one_point_crossover(100))
    assert len(mask) == 100
    mask_iter = iter(mask)

    mask_run(mask_iter, True)

    for m in mask_iter:
        assert m is False


def test_two_point_crossover():
    mask = list(cross.two_point_crossover(100))
    assert len(mask) == 100
    mask_iter = iter(mask)

    mask_run(mask_iter, True)
    mask_run(mask_iter, False)

    for m in mask_iter:
        assert m is True


def test_uniform_point_crossover():
    mask = list(cross.uniform_point_crossover(100))
    assert len(mask) == 100

    values = set()
    for m in mask:
        values.add(m)
    assert True in values and False in values
