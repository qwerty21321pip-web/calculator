import pytest

from calculator.core import add, subtract, multiply, divide, power


@pytest.mark.parametrize("a,b,expected", [(2,3,5), (-2,3,1), (0,0,0), (1.5,2.5,4)])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        divide(1, 0)


@pytest.mark.parametrize("a,b,expected", [(2,3,8), (5,0,1), (2,-2,0.25)])
def test_power(a, b, expected):
    assert power(a, b) == pytest.approx(expected)
