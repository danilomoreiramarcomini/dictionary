dictionary = dict()

for value in range(9, 0, -1):
    dictionary[f'{value}ª Key'] = str(f'{value}º Value')

for key, value in sorted(dictionary.items()):
    print(f'{key}: {value}')
