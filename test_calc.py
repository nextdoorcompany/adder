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
    ])
def test_get_inch_decimal_decimal_input(test_input, tolerance, expected):
    result = calc.get_inch_decimal(test_input, tolerance)
    assert result == expected
