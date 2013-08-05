from nose.tools import assert_raises
from genetics.dna.component import DNAComponent

# Classes for test cases
class BasicComponent1(DNAComponent):
    def initial_value(self):
        return 1


class BasicComponent2(DNAComponent):
    def initial_value(self):
        return 2


class ComponentWithIterable(DNAComponent):
    def initial_value(self):
        return (1, 2, 3, 4)


class IncrementingComponent(DNAComponent):
    def initial_value(self):
        return 0

    def mutate_value(self):
        return self.value + 1


class ComponentNoInitial(DNAComponent):
    def mutate_value(self):
        return 1


def test_initial_value():
    x = DNAComponent(5)
    assert x.value == 5


def test_initial_value_from_function():
    x = BasicComponent1()
    assert x.value == 1


def test_initial_value_from_mutation():
    x = ComponentNoInitial()
    assert x.value == 1


def test_initial_value_no_arg_fails():
    with assert_raises(AttributeError):
        DNAComponent()


def test_total_length_basic():
    basic = BasicComponent1()
    assert basic.total_length() == 1


def test_total_length_iterable():
    iterable = ComponentWithIterable()
    assert iterable.total_length() == 1


def test_mutation():
    original_component = IncrementingComponent()
    component = original_component
    assert component.value == 0
    component = component.mutate([1])
    assert component.value == 1
    component = component.mutate([0])
    assert component.value == 1
    component = component.mutate([1, 0])
    assert component.value == 2
    component = component.mutate([0, 1])
    assert component.value == 2
    assert original_component.value == 0


def test_mask_consumption():
    component = IncrementingComponent()

    mask = iter((True, False, True, False))
    assert component.value == 0
    component = component.mutate(mask)
    assert component.value == 1
    assert next(mask) == False


def test_combine():
    def combine_check(mask, did_swap):
        child1, child2 = parent1.combine(parent2, mask)
        if did_swap:
            assert child1.value == parent1.value
            assert child2.value == parent2.value
        else:
            assert child1.value == parent2.value
            assert child2.value == parent1.value

    parent1 = BasicComponent1()
    parent2 = BasicComponent2()

    combine_check([True], True)
    combine_check([False], False)
    combine_check([True, False], True)
    combine_check([False, True], False)
