def merge(values):      # values - это список словарей
    res = {}
    for d in values:
        for key in d:
            if d[key] not in res.get(key, []):
                res.setdefault(key, set()).add(d[key])

    return res

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
print(result)