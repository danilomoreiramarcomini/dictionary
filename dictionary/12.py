dictionary = dict()

for value in range(1, 11):
    dictionary[f'{value}'] = value

remove_key = str(input('Type the key to remove:')).lower()

dictionary.pop(f'{remove_key}')

print(f'{dictionary}')
