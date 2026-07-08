def greet(name):
    return f"Hello, {name}!"
def is_even(num):
    return num % 2 == 0

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(greet("Alice"))
