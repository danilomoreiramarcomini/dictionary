import random

values = dict()
values_sorted = dict()
values_sorted_reverse = dict()
for e in range(1, 11):
    values[f'{e}º value'] = random.randint(0, 999)

values_sorted_by_value = sorted(values, key=values.get)
values_sorted_by_value_reverse = sorted(values, key=values.get, reverse=True)

for element in values_sorted_by_value:
    values_sorted[element] = values[element]

for element in values_sorted_by_value_reverse:
    values_sorted_reverse[element] = values[element]

for value in values_sorted.values():
    print(f'{value}', end=' ')

print('\n')

for value in values_sorted_reverse.values():
    print(f'{value}', end=' ')
