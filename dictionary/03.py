dictionary_a = {1: 10, 2: 20}
dictionary_b = {3: 30, 4: 40}
dictionary_c = {5: 50, 6: 60}
dictionary_d = dict()

dictionary_d.update(dictionary_a)
dictionary_d.update(dictionary_b)
dictionary_d.update(dictionary_c)

print(dictionary_d)
