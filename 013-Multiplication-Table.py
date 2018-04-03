
n = int(input('Which multiplication table do you want to do?: '))

for i in range(1, 11):
    print('{0} x {1} = {2}'.format(i, n, i * n))
