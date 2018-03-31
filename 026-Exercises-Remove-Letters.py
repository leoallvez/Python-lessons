text1 = input('Text one: ')
text2 = input('Text two: ')

result = text1

for t1 in text1:
    for t2 in text2:
        if t1 == t2:
            result = result.replace(t1, "")

print(result)

