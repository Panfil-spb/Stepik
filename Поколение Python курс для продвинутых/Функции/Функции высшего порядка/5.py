def func_apply(func, elements):
    res = []
    for i in elements:
        res.append(func(i))
    return res