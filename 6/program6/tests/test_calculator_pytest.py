import pytest
from calculator import *
from math import isclose

@pytest.fixture
def calc():
    return Calculator()

# --- add ---
@pytest.mark.parametrize(
    "args, expected",
    [
        ((0,), 0),
        ((1, 2), 3),
        ((-5, 5), 0),
        ((1.5, 2.5), 4.0),
        ((1, 2, 3, 4), 10),
        ((-1, -2, -3), -6),
        ((1000000, 1), 1000001),
    ],
)
def test_add(calc, args, expected):
    assert calc.add(*args) == expected

# --- divide: корректные кейсы ---
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (-9, 3, -3),
        (7, 2, 3.5),
        (1.0, 4, 0.25),
    ],
)
def test_divide_ok(calc, a, b, expected):
    result = calc.divide(a, b)
    # для float лучше isclose
    if isinstance(expected, float):
        assert isclose(result, expected)
    else:
        assert result == expected

# --- divide: исключение при делении на ноль ---
@pytest.mark.parametrize("a", [0, 1, -5, 3.14])
def test_divide_by_zero_raises(calc, a):
    with pytest.raises(ZeroDivisionError):
        calc.divide(a, 0)

# --- is_prime_number ---
@pytest.mark.parametrize(
    "n, expected",
    [
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (16, False),
        (17, True),
        (19, True),
        (21, False),
        (97, True),
        (100, False),
    ],
)
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected
