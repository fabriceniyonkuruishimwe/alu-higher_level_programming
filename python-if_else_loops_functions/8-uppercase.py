#!/usr/bin/python3


def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print("{}".format(result))
