def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def imprint(a, b, func):
    print(func(a, b))


imprint(5, 4, add)
imprint(22, 1, subtraction)

