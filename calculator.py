# https://github.com/MahiB-sudo/lab11-MB-RM
# Partner 1: Mahiba Bhuiyan
# Partner 2: Ross Modur

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(a)
    except ValueError:
        raise


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError:
        raise

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def logarithm(a, b):
    return log(a, b)

def exp(a, b):
    return a ** b