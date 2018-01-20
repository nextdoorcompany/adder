import calc


def test_get_inch_decimal_zero():
    result = calc.get_inch_decimal('0')
    assert result == 0


def test_get_inch_decimal_inch_negative():
    result = calc.get_inch_decimal('-4.313')
    assert result == -4.3125


def test_get_inch_decimal_inch_positve():
    result = calc.get_inch_decimal('17')
    assert result == 17


def test_get_inch_decimal_inch_precision():
    result = calc.get_inch_decimal('33.047')
    assert result == 33.046875


def test_get_inch_decimal_inch_round_up():
    result = calc.get_inch_decimal('0.993')
    assert result == 1


def test_get_inch_decimal_inch_round_down():
    result = calc.get_inch_decimal('1.007')
    assert result == 1


def test_get_inch_decimal_inch_round_up_at_half():
    result = calc.get_inch_decimal(str(127/128))
    assert result == 1
