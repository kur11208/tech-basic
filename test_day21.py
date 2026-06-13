# Day 21: pytest tests

from day21 import calculate_value


def test_calculate_value():
    assert calculate_value(1000, 3) == 3000
    assert calculate_value(500, 0) == 0
    assert calculate_value(1200, 1) == 1200
