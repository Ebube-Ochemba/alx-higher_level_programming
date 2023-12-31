#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {:s}".format(str(error)), file=sys.stderr)
        return False
