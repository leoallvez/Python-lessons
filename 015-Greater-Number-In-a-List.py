numberList = [92, 22, 2, 5, 9, 10, 12, 76, 8, 23]

maximum = numberList[0]
for number in numberList:
    if number > maximum:
        maximum = number
print(maximum)
