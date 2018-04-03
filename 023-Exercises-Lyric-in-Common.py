text1 = input('Text One: ')
text2 = input('Text two: ')

new_list = []

for l1 in text1:
    for l2 in text2:
        if l1.upper() == l2.upper():
            new_list.append(l1)

if new_list:
    print('letras em comum {} '.format(''.join(new_list)))
else:
    print('nenhuma letra em comum')
