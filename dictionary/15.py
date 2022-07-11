dictionary = dict()
list_values = list()
for element in range(1, 1001):
    dictionary[f'{element}ª Key'] = str(f'{element}')

for value in dictionary.values():
    list_values.append(value)

max_value = max(list_values)
min_value = min(list_values)

for key, value in dictionary.items():
    if value == max_value:
        print(f'Maximum: Key: {key} Value: {value}')
    if value == min_value:
        print(f'Minimum: Key: {key} Value: {value}')
