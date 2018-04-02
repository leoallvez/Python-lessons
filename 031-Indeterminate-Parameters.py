def soma(*args):
    s = 0
    for x in args:
        s = s + x
    return s


print(soma(1))
print(soma(2, 2))
print(soma(1, 2, 4, 8, 8, 9, 9, 7))
