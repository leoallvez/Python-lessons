text = input('Text: ')
letters = {}

for l in text:
    if l in letters:
        letters[l][1] += 1
    else:
        letters[l] = [l, 1]

for key in letters:
    print('{0}: {1}x'.format(key.upper(), letters[key][1]))
