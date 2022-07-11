dictionary = dict()

for value in range(0, 11):
    dictionary[f'{value}'] = value

print(f'{sum(dictionary.values())}')
