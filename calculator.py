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

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError("Invalid logarithm arguments")

def exponent(a, b):
    return a ** b