#!/usr/bin/python3
import sys
"""
    Description of function :
    Calculates the factorial of a given integer.
    The factorial of a number n, denoted as n!, is the product of all integers
    from 1 to n. By definition, the factorial of 0 is 1.

    Parameters:
    n (int): An integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the number n. If n is 0, returns 1.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
