from ht1 import square_square, rectangle_square, storage
import pytest

@pytest.mark.parametrize(
    "a, expected",
    [
        (4, 16),
        (5, 25),
        (10, 100),
    ]
)
def test_square_square(a, expected):
    assert square_square(a) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 5, 20),
        (2, 10, 20),
        (7, 3, 21),
    ]
)
def test_rectangle_square(a, b, expected):
    assert rectangle_square(a, b) == expected


@pytest.mark.parametrize(
    "salary, percent_mortgage, percent_life, expected",
    [
        (100000, 20, 50, 360000),
        (200000, 10, 50, 960000)
    ]
)
def test_storage_func(salary, percent_mortgage, percent_life, expected):
    assert storage(salary, percent_mortgage, percent_life,) == expected