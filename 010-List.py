List = [1, 3, 4, 7, 9, 0, 2, 5]
p = int(input('Number to find: '))
for e in List:
    if e == p:
        print('number found: {0}'.format(e))
        break
print('number not found')
