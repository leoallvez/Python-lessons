grades = [0, 0, 0, 0, 0]
result = 0
x = 0
while x < 5:
    grades[x] = float(input('Grade {0}: '.format(x)))
    result += grades[x]
    x += 1
x = 0
while x < 5:
    print('Grade :{0}'.format(x))
    x += 1
print('Average: {0}'.format(result/x))
