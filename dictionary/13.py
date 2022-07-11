keys = list()
values = list()

for value in range(1, 10):
    keys.append(f'{value}')
    values.append(value)

dictionary = dict(zip(keys, values))

print(dictionary)
