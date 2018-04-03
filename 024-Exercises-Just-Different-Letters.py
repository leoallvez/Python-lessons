text1 = input('Text one ')
text2 = input('Text two ')

new_text = text1 + text2
initial_size = len(new_text)

for s1 in text1:
    for s2 in text2:
        if s1 == s2:
            new_text = new_text.replace(s1, "")
if initial_size > len(new_text):
    print('letras diferentes nos dois textos ({})'.format(new_text))
else:
    print('os dois textos não tem letras em comum')

