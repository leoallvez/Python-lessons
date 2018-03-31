name = 'Leonardo Alves'
has_first_name = name.startswith('Leonardo')
has_last_name = name.endswith('Alves')
print('The name starts with Leonardo?: {} \n And ends with Alves {}'.format(has_first_name, has_last_name))

print(name.lower())

print(name.upper())

print(name.upper().startswith('LEONARDO'))

print('Leonardo' in name)
print('Fernando' in name)
print('LEO' in name.upper())
print('Maria' not in name)

t = 'One Tiger two Tigers three tigers'
print(t.upper().count('TIGER'))
print(t.upper().find('THREE'))
