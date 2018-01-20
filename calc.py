import re


TOL = 64


def cli():
    register_inch_decimal = 0
    while True:
        cmd = input('>')
        # intercept commands
        opr_inch_decimal = get_inch_decimal(cmd)
        register_inch_decimal = add(register_inch_decimal, opr_inch_decimal)
        print(output(register_inch_decimal))


def get_inch_decimal(cmd_as_text):
    # inch decimal [-]0+[.0*]
    if re.fullmatch(r'-?\d+(\.\d*)?', cmd_as_text):
        result = float(cmd_as_text)
        result = round(TOL * result) / TOL
        return result

    # inch fraction [-]0+ 0+/0+ or [-]0+/0+

    # ft inch fraction [-]0+-0+[ 0+/0+]


def add(register_inch_decimal, opr_inch_decimal):
    pass


def output(register_inch_decimal):
    pass


if __name__ == "__main__":
    cli()
