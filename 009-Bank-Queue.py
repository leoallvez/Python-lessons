last = 10
queue = list(range(1, last+1))
while True:
    print('There are {0} customers in the queue.'.format(len(queue)))
    print('Current row:', queue)
    print('Type F to add a client to the end of the queue,')
    print('or A to perform the service')
    operation = input('operation (F, A, or S): ')
    if operation == 'A':
        if len(queue) > 0:
            attended = queue.pop(0)
            print('Customer {0} served'.format(attended))
        else:
            print('Empty row no one to answer.')
    elif operation == 'F':
        last += 1
        queue.append(last)
    elif operation == 'S':
        break
    else:
        print('Invalid operation! enter only F, A or S!')
