"""Session 2 Homework: Decorators and Generators."""

import math


def validate_positive(func):
    """Raise ValueError if the input number is negative."""

    def wrapper(n):
        if n < 0:
            raise ValueError("Number cannot be negative.")
        return func(n)

    return wrapper


@validate_positive
def square_root(n):
    """Return the square root of a positive number."""
    return math.sqrt(n)


def countdown(n):
    """Generate a countdown from n to 0."""
    while n >= 0:
        yield n
        n -= 1


print("Square Root Demo")
print(square_root(-9))

print("\nLaunch Countdown")
for number in countdown(5):
    print(number)
