text1 = input('Text one: ')
text2 = input('Text two: ')

result = text1.upper().find(text2.upper())
if result > -1:
    print('text {} is in text {} of item {}'.format(text2, text1, result))
else:
    print('text [{}] not found in text {}'.format(text2, text1))
