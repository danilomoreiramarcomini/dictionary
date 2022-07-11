import random

dictionary = dict()
number = int(input('Type a value:'))

for element in range(1, number + 1):
    dictionary[f'{element}'] = random.randint(1, 100)

for key, value in dictionary.items():
    print(f'{key}: {value}')
