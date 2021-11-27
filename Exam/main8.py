a = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
b = {k: v for k, v in a.items() if v > 2}
print(b)