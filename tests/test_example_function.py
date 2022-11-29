import math

from python_pkg_template.example_function import add_two_values, using_numpy


def test_add_two_values():
    assert add_two_values(2, 3) == 5


def test_using_numpy():
    assert math.isclose(math.pi, using_numpy())
