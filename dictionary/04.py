dictionary = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60}


while True:
    number = str(input('Type a number or q to quit:'))

    if number in 'qQ':
        break

    if number in dictionary:
        print(f'{number} is present in the dictionary')

    else:
        print(f'{number} is not present in the dictionary')
