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

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b