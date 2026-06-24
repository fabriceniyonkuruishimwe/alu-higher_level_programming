#!/usr/bin/python3


def fizzbuzz():
    """Print numbers 1 to 100, Fizz for multiples of 3,
    Buzz for multiples of 5, FizzBuzz for both."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")
