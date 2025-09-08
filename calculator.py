def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b and return the result."""
    return a ** b


def square_root(a):
    """Return the square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5


def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def percentage(value, total):
    """Calculate what percentage value is of total."""
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100