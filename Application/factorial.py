def factorial(n):
    if isinstance(n, str):
        return "Invalid Input"

    elif n < 0:
        return "Invalid Input"

    elif n == 0:
        return 1
    return int(n) * factorial (int(n)-1)