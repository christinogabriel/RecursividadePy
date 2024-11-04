def produtório(n):
    if n == 0:
        return 1
    return n * produtório(n - 1)
