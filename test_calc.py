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


@pytest.mark.parametrize('op1,op2,expected', [
    (2, 2, 4),
    (2.5, 2, 4.5),
    (-0.5, 2, 1.5),
    (-6, -3, -9),
    (0, 0, 0),
    (-3, 5, 2),
    (5, -3, 2),
    (0.25, 0.375, 0.625),
    (-0.25, -0.375, -0.625),
    (0.25, -0.375, -0.125),
    ])
def test_add(op1, op2, expected):
    result = calc.add(op1, op2)
    assert result == expected


@pytest.mark.parametrize('test_input,tolerance,places,expected', [
    (4.5, 64, 3, '4.5'),
    (4.5625, 64, 3, '4.562'),
    (-3.5, 64, 2, '-3.5'),
    (0, 64, 3, '0.0'),
    (-3, 64, 3, '-3.0'),
    (1.75, 64, 0, '2.0'),
    (1.5625, 2, 3, '1.5'),
    (0.015625, 32, 3, '0.0'),
    (143.375, 64, 3, '143.375'),
    (-0.59375, 64, 3, '-0.594'),
    ])
def test_get_decimal_places(test_input, tolerance, places, expected):
    result = calc.get_decimal_at_places(test_input, tolerance, places)
    assert result == expected


@pytest.mark.parametrize('test_input,tolerance,expected', [
    (0.59375, 64, '0 19/32'),
    (-0.59375, 64, '-0 19/32'),
    (7.6875, 64, '7 11/16'),
    (-4.375, 64, '-4 3/8'),
    (5.015625, 64, '5 1/64'),
    (9.375, 2, '9 1/2'),
    (0, 64, '0'),
    (4, 64, '4'),
    (-4, 64, '-4'),
    ])
def test_get_fraction(test_input, tolerance, expected):
    result = calc.get_fraction(test_input, tolerance)
    assert result == expected


@pytest.mark.parametrize('test_input,tolerance,expected', [
    (36, 64, '3-0'),
    (-36, 64, '-3-0'),
    (5.6875, 64, '0-5 11/16'),
    (-5.6875, 64, '-0-5 11/16'),
    (88.375, 2, '7-4 1/2'),
    (-52.015625, 64, '-4-4 1/64'),
    (42, 64, '3-6'),
    (99, 64, '8-3'),
    ])
def test_get_ft_inch(test_input, tolerance, expected):
    result = calc.get_ft_inch(test_input, tolerance)
    assert result == expected
