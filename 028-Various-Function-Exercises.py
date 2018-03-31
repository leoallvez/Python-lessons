def return_the_largest(a, b):
    return a if a > b else b


print(return_the_largest(5, 6))
print(return_the_largest(2, 1))
print(return_the_largest(7, 7))


def its_multiple(a, b):
    return a % b == 0


print(its_multiple(8, 4))
print(its_multiple(7, 3))
print(its_multiple(5, 5))


def square_area(side):
    return side ** 2


print(square_area(4))
print(square_area(9))


def triangle_area(base, height):
    return (base * height) / 2


print(triangle_area(6, 9))
print(triangle_area(5, 8))
