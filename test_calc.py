import pytest
import calc


@pytest.mark.parametrize('test_input,tolerance,expected', [
    ('0', 64, 0),
    ('-4.313', 64, -4.3125),
    ('17', 64, 17),
    ('33.047', 64, 33.046875),
    ('0.993', 64, 1),
    ('1.007', 64, 1),
    (str(127/128), 64, 1),
    ('0.688', 2, 0.5),
    ('.125', 64, 0.125),
    ('-.125', 64, -0.125),
    ])
def test_get_inch_decimal_decimal_input(test_input, tolerance, expected):
    result = calc.get_inch_decimal(test_input, tolerance)
    assert result == expected


@pytest.mark.parametrize('test_input,tolerance,expected', [
    ('0 19/32', 64, 0.59375),
    ('-0 19/32', 64, -0.59375),
    ('19/32', 64, 0.59375),
    ('-19/32', 64, -0.59375),
    ('7 11/16', 64, 7.6875),
    ('-4 3/8', 64, -4.375),
    ('5 1/64', 64, 5.015625),
    ('9 3/8', 2, 9.5),
    ])
def test_get_inch_decimal_fraction_input(test_input, tolerance, expected):
    result = calc.get_inch_decimal(test_input, tolerance)
    assert result == expected


@pytest.mark.parametrize('test_input,tolerance,expected', [
    ('3-0', 64, 36),
    ('-3-0', 64, -36),
    ('0-5 11/16', 64, 5.6875),
    ('-0-5 11/16', 64, -5.6875),
    ('7-4 3/8', 2, 88.5),
    ('-4-4 1/64', 64, -52.015625),
    ('3-6', 64, 42),
    ('8-3', 64, 99),
    ])
def test_get_inch_decimal_foot_inch_input(test_input, tolerance, expected):
    result = calc.get_inch_decimal(test_input, tolerance)
    assert result == expected
