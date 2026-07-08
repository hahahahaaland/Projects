"""A simple Python program demonstrating basic functions."""
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def is_even(num):
    """Return True if the number is even."""
    return num % 2 == 0


def factorial(n):
    """Return the factorial of a non-negative integer."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(greet("Vanshika"))
