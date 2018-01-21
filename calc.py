import re


def cli(input_tolerance=64, output_tolerance=64):
    register_inch_decimal = 0
    while True:
        cmd = input('>')
        # intercept commands
        opr_inch_decimal = get_inch_decimal(cmd, input_tolerance)
        register_inch_decimal = add(register_inch_decimal, opr_inch_decimal)
        print(output(register_inch_decimal))


def get_inch_decimal(cmd_as_text, tolerance):
    if re.fullmatch(r'-?\d*(\.\d*)?', cmd_as_text):
        result = float(cmd_as_text)
        return round_to_nearest(result, tolerance)

    if re.fullmatch(r'-?\d+ \d+/\d+|-?\d+/\d+', cmd_as_text):
        spc = cmd_as_text.find(' ')
        slash = cmd_as_text.find('/')
        if spc > 0:
            whole = int(cmd_as_text[0:spc])
            numerator = int(cmd_as_text[spc+1:slash])
            if cmd_as_text[0] == '-':
                numerator = numerator * -1
        else:
            whole = 0
            numerator = int(cmd_as_text[:slash])
        denominator = int(cmd_as_text[slash+1:])
        result = whole + (numerator / denominator)
        return round_to_nearest(result, tolerance)

    if re.fullmatch(r'-?\d+-\d+( \d+/\d+)?', cmd_as_text):
        sep = cmd_as_text.find('-', 1)
        feet = int(cmd_as_text[0:sep])
        inch_text = cmd_as_text[sep+1:]
        if cmd_as_text[0] == '-':
            inch_text = '-' + inch_text
        inches = get_inch_decimal(inch_text, tolerance)
        return (feet * 12) + inches


def add(register_inch_decimal, opr_inch_decimal):
    pass


def output(register_inch_decimal):
    pass


def round_to_nearest(value, tolerance):
    return round(tolerance * value) / tolerance


if __name__ == "__main__":
    cli()
