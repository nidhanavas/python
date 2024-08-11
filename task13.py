d = {'pencil': 10, 'pen': 20, 'book': 30, 'comb': 40, 'pot': 50}
max_key = next(iter(d))
for key in d:
     if d[key] > d[max_key]:
        max_key = key
print(max_key)