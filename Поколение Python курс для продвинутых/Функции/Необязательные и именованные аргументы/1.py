def matrix(n=None, m=None, value=0):
    if n is None and m is None:
        return [[0]]
    elif n is not None and m is None:
        return [[value for i in range(n)] for j in range(n)]
    else:
        return [[value for j in range(m)] for i in range(n)]

