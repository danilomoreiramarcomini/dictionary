dictionary = dict()
support = int(1)
for value in range(1, 11):
    dictionary[f'{dictionary}ª Key'] = value

for value in dictionary:
    support = support * dictionary[value]

print(support)
