def build_query_string(params):
    params_sort = sorted(params)
    s = '&'.join(i + '=' + str(params[i]) for i in params_sort)

    return s

print(build_query_string({'name': 'timur', 'age': 28}))